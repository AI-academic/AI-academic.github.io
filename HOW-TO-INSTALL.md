# What to do with each file

Four kinds of file. Only the first kind changes day to day.

## 1. `_items/` — one file per news story (39 of them)

Upload the whole `_items` folder. Each file is one story: its own date, the
briefing that carried it, its section, tags, organizations and source links.
This is the only folder you add to when publishing.

## 2. `_posts/` — seven four-line wrappers (REPLACES your current posts)

Same filenames as your existing posts, so uploading them overwrites the old
ones and every published URL is preserved. The prose that used to live in
these files now lives in `_items/`. Only the September 2 wrapper keeps body
text, because that issue had an introductory note.

## 3. Machinery — upload once, then never touch

`_config.yml` (replaces yours)
`_data/organizations.yml`
`_includes/item.html`
`_includes/briefing-body.html`
`_layouts/briefing.html`
`index.html` (replaces yours)
`topics.html`
`organizations.html`
`search.html`
`search.json`
`archive.md`

If you still have an `index.md`, delete it — a repo cannot hold both it and
`index.html`.

`_data/organizations.yml` is the one machinery file you will edit again: add a
line whenever a new organization appears.

## 4. Reference — for you, not for the site

`TAGS.md` and this file. They sit in the repo so they are there when you
need them. They are not published as pages.

There is deliberately no separate list of organization names: that list is
`_data/organizations.yml` itself, which the site reads and you read. Keeping
a second copy would only give you two lists that disagree.

---

## Order of upload

1. `_config.yml`
2. `_data/`, `_includes/`, `_layouts/`
3. `index.html`, `topics.html`, `organizations.html`, `search.html`,
   `search.json`, `archive.md` — and delete `index.md` if present
4. `_items/`
5. `_posts/` (overwriting the seven existing files)

Then watch the Actions tab. When it goes green, check in this order:
the front page, `/topics/`, `/organizations/`, `/search/`, and one old
briefing such as `/2026/08/27/briefing/`.

On `/organizations/`, an **Unclassified** heading at the foot means a name in
an item is missing from `_data/organizations.yml`. On `/topics/`, a line at
the foot means a tag is missing from `tag_vocabulary` in `_config.yml`.
Both are meant to be seen and fixed, not ignored.

## After the install

Delete this file. Everything in it that stays true — the repository map, the
publishing routine, the conventions — is in `README.md`, which is what the
repository page shows and what you will actually come back to.

## Publishing a new briefing after this

1. One file per story in `_items/YYYY-MM-DD/`, where the folder is the date
   of the briefing.
2. One wrapper in `_posts/YYYY-MM-DD-briefing.md`.
3. If a story names an organization you have not used before, add it to
   `_data/organizations.yml` with its kind.

Everything else — front page, topic pages, organization pages, search index,
RSS — rebuilds itself.
