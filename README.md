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
sources:
  - label: "Cornell hopes to turn cheating into a teachable moment"
    url: "https://www.insidehighered.com/news/students/academics/..."
---
Body prose, in markdown.
```

`date` and `briefing` are separate on purpose: an issue routinely carries news
from the preceding week. Topic and organization pages sort by when the news
happened; briefing pages gather by when it was published.

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
- **Sections** are `ontario`, `canada`, `international`, `government`,
  `sector`, `other`, defined in `_config.yml`.

## When something is wrong

Mistakes are made visible rather than silent:

- A tag missing from the vocabulary is named at the foot of `/topics/`.
- An organization missing from the registry appears under **Unclassified**
  at the foot of `/organizations/`.
- An item with an unrecognised `section` appears under **Unfiled** at the
  foot of its briefing.
- An item that does not appear at all is usually a filename or date problem:
  `_posts` filenames must be `YYYY-MM-DD-name.md` with hyphens, and an item's
  `briefing` date must match a post that exists.

Build failures are reported in the repository's **Actions** tab, with the file
and line.
