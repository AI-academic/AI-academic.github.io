# AI-academic.github.io

AI related news and development relevant to academic institutions.
Published at **https://ai-academic.github.io/**

A curated briefing. Each news story is a separate file; a briefing for a given
date is assembled from the stories that carry that date. That is what lets the
same story appear in its briefing, under each of its topics, under each
organization it concerns, and in search — without being written more than once.

## Publishing a briefing

1. One file per story in `_items/YYYY-MM-DD/`, where the folder is the date of
   the briefing.
2. One wrapper post in `_posts/YYYY-MM-DD-briefing.md` — four lines, plus an
   introductory note if the issue needs one.
3. If a story names an organization not yet used, add it to
   `_data/organizations.yml` with its kind.

The front page, briefing pages, topic pages, organization pages, the search
index and the RSS feed all rebuild themselves. Nothing else is edited by hand.

### An item file

```yaml
---
title: "Cornell diverts minor integrity violations out of formal hearings"
date: 2026-08-24            # when the news happened
briefing: 2026-09-02        # which issue carried it
slug: cornell-integrity     # sets the anchor; keep it short and stable
section: international
tags: [assessment, governance]
organizations:
  - "Cornell University"
related: [nature-ai-detection-tools]   # optional; slugs of other items
sources:
  - label: "Cornell hopes to turn cheating into a teachable moment"
    url: "https://www.insidehighered.com/news/students/academics/..."
---
Body prose, in markdown.
```

`date` and `briefing` are separate on purpose: an issue routinely carries news
from the preceding week. Topic and organization pages sort by when the news
happened; briefing pages gather by when it was published.

`related` is optional and reciprocal. Name another item's slug and both items
show a link to the other, so a pairing is recorded once — on whichever item was
written second — and never has to be maintained in two places. Two related
items are usually plenty; the line is for a reader who wants the earlier story,
not a see-also index.

## What is where

| Path | What it is |
|---|---|
| `_items/` | Every news story, one file each. The only folder that grows. |
| `_posts/` | One short wrapper per briefing date. |
| `_data/organizations.yml` | Every organization and its kind. Read it before typing a name. |
| `_config.yml` | Site settings, the section list, the tag vocabulary. |
| `_includes/`, `_layouts/` | Assembly machinery. Not edited. |
| `index.html`, `topics.html`, `organizations.html`, `search.html`, `search.json`, `archive.md` | The pages. Not edited. |
| `TAGS.md` | What each tag means, and the rule for reviewing the vocabulary. |

## Conventions

- **Tags** come from a fixed list in `TAGS.md` and `tag_vocabulary` in
  `_config.yml`. Two to four per item. Do not invent one mid-issue.
- **Organizations** are the actors in a story, not every name mentioned.
  Copy the spelling from `_data/organizations.yml`.
- **Sections** are `canada`, `international`, `government`,
  `other`, defined in `_config.yml`.
- **Related items** are named by slug, never by title, and only in one
  direction. The reverse link appears on its own.
- **Sources** go primary document first, later coverage after. A second source
  has to add something the first does not, and its label has to say what:
  "Companion release" tells a reader nothing, "Companion release: UK access to
  Ukraine's AI labs" tells them whether to click. One source renders inline;
  two or more are stacked as a list with their domains, so the label is what
  the reader chooses on.

## Announcing an issue by email

A workflow in `.github/workflows/announce-issue.yml` mails the briefing list
whenever a **new** file appears in `_posts/`. Editing an existing issue sends
nothing. It waits for GitHub Pages to publish the issue before sending, so the
link in the message is live on arrival, and it composes the message from the
repository itself -- the same issue label the site shows, and every story
headline grouped into the standing sections.

Set up once, in Settings -> Secrets and variables -> Actions:

| Secret | What it is |
|---|---|
| `MAIL_USERNAME` | the Gmail address that sends |
| `MAIL_APP_PASSWORD` | a Gmail app password, which needs 2-Step Verification |
| `LIST_ADDRESS` | the Google Group address the mail goes to |

The list itself lives in the Google Group, not in this repository -- joining and
leaving are handled there, and no subscriber address is ever stored here. That
matters because this repository is public.

To resend an issue, or to send one the workflow missed, use **Run workflow** on
the Actions tab and give a date such as `2026-09-12`.

## When something is wrong

Mistakes are made visible rather than silent:

- A tag missing from the vocabulary is named at the foot of `/topics/`.
- An organization missing from the registry appears under **Unclassified**
  at the foot of `/organizations/`.
- An item with an unrecognised `section` appears under **Unfiled** at the
  foot of its briefing.
- A `related` slug that matches no item is printed under the item as
  unresolved, so a typo or a renamed slug shows up on the page.
- An item that does not appear at all is usually a filename or date problem:
  `_posts` filenames must be `YYYY-MM-DD-name.md` with hyphens, and an item's
  `briefing` date must match a post that exists.

Build failures are reported in the repository's **Actions** tab, with the file
and line.
