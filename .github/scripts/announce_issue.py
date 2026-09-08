#!/usr/bin/env python3
"""Email the briefing list when a new issue is published.

Reads the repository rather than the built site, so the message says the same
thing the pages do: the issue label is composed the way _includes/issue-label.html
composes it, and the story list comes from the item files themselves.

Standard library only -- no packages to install and nothing to keep updated.
"""

import os
import re
import smtplib
import ssl
import subprocess
import sys
import time
import urllib.request
from datetime import date
from email.message import EmailMessage
from email.utils import formatdate
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE_URL = "https://ai-academic.github.io"
WAIT_SECONDS = 600          # how long to wait for Pages to publish the issue
POLL_SECONDS = 20


def log(msg):
    print(msg, flush=True)


def issue_dates():
    """Every issue date in the repository, oldest first."""
    return sorted(p.name[:10] for p in (ROOT / "_posts").glob("*.md"))


def added_post_date():
    """The date of a post file ADDED by this push, if there is one."""
    before, after = os.environ.get("BEFORE_SHA", ""), os.environ.get("AFTER_SHA", "")
    if not before or not after or set(before) == {"0"}:
        return None
    try:
        out = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=A", before, after, "--", "_posts"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout
    except subprocess.CalledProcessError as exc:
        log(f"Could not diff {before}..{after}: {exc}")
        return None
    names = sorted(Path(n).name[:10] for n in out.split() if n.endswith(".md"))
    return names[-1] if names else None


def sections():
    """Section keys and labels, in order, from _config.yml."""
    cfg = (ROOT / "_config.yml").read_text(encoding="utf-8")
    block = cfg.split("sections:", 1)[1].split("tag_vocabulary:", 1)[0]
    return re.findall(r'- key: (\w+)\s*\n\s*label: "([^"]+)"', block)


def field(text, name):
    m = re.search(rf'(?m)^{name}: (.+)$', text)
    return m.group(1).strip().strip('"') if m else ""


def gather(issue):
    """The issue's note and its stories, grouped into the standing sections."""
    post = ROOT / "_posts" / f"{issue}-briefing.md"
    if not post.exists():
        sys.exit(f"No post file for {issue}; nothing to announce.")
    note = post.read_text(encoding="utf-8").split("---", 2)[2].strip()

    stories = {}
    for path in sorted((ROOT / "_items" / issue).glob("*.md")) if (ROOT / "_items" / issue).is_dir() else []:
        front = path.read_text(encoding="utf-8").split("---", 2)[1]
        stories.setdefault(field(front, "section"), []).append(
            (field(front, "title"), field(front, "slug") or path.stem)
        )
    return note, stories


def label(issue, count):
    number = issue_dates().index(issue) + 1
    d = date.fromisoformat(issue)
    when = f"{d.strftime('%B')} {d.day}, {d.year}"
    return f"Issue {number} · {when} · {count} update{'' if count == 1 else 's'}"


def wait_for(url):
    """Give Pages time to publish before mailing a link to it."""
    deadline = time.time() + WAIT_SECONDS
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=15) as r:
                if r.status == 200:
                    log(f"{url} is live.")
                    return True
        except Exception as exc:
            log(f"waiting for {url} ({exc.__class__.__name__})")
        time.sleep(POLL_SECONDS)
    log(f"{url} did not appear within {WAIT_SECONDS}s; sending anyway.")
    return False


def bodies(issue, note, stories, url, subject):
    order = sections()
    text = [subject, "", note] if note else [subject, ""]
    html = [f"<h2 style='margin:0 0 .3em'>{subject}</h2>"]
    if note:
        html.append(f"<p>{note}</p>")

    for key, heading in order:
        rows = stories.get(key, [])
        if not rows:
            continue
        text += ["", heading.upper()]
        html.append(f"<h3 style='margin:1.2em 0 .3em'>{heading}</h3><ul>")
        for title, slug in rows:
            text.append(f"  - {title}")
            html.append(f"<li><a href='{url}#{slug}'>{title}</a></li>")
        html.append("</ul>")

    text += ["", f"Read the issue: {url}", "", f"All issues: {SITE_URL}/archive/"]
    html.append(
        f"<p style='margin-top:1.5em'><a href='{url}'>Read the issue on the site</a>"
        f" &middot; <a href='{SITE_URL}/archive/'>all issues</a>"
        f" &middot; <a href='{SITE_URL}/feed.xml'>RSS</a></p>"
    )
    return "\n".join(text), "\n".join(html)


def main():
    issue = (os.environ.get("ISSUE_DATE") or "").strip() or added_post_date()
    if not issue:
        log("This push added no new issue; nothing to send.")
        return
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", issue):
        sys.exit(f"'{issue}' is not a date in YYYY-MM-DD form.")

    note, stories = gather(issue)
    count = sum(len(v) for v in stories.values())
    if count == 0:
        sys.exit(f"{issue} has no items; refusing to announce an empty issue.")

    subject = label(issue, count)
    url = f"{SITE_URL}/{issue.replace('-', '/')}/briefing/"
    log(f"Announcing: {subject}\n{url}")
    wait_for(url)

    user = os.environ["MAIL_USERNAME"]
    password = os.environ["MAIL_APP_PASSWORD"]
    to = os.environ["LIST_ADDRESS"]

    text, html = bodies(issue, note, stories, url, subject)
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = to
    msg["Date"] = formatdate(localtime=True)
    msg.set_content(text)
    msg.add_alternative(
        "<div style=\"font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;"
        "font-size:15px;line-height:1.5;max-width:38em\">" + html + "</div>",
        subtype="html",
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as s:
        s.login(user, password)
        s.send_message(msg)
    log(f"Sent to {to}.")


if __name__ == "__main__":
    main()
