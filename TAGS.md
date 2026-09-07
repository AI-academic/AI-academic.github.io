# Tag vocabulary

Fixed list. Consult this file while tagging; do not invent a tag mid-issue.
Two to four tags per item. The test for applying one: would a reader who
follows this tag be glad this item turned up?

| Tag | Covers |
|---|---|
| `policy` | External rules: legislation, regulators, courts, accreditation bodies, intergovernmental guidance |
| `governance` | Internal decisions: institutional policy, strategy documents, new units and mandates, oversight |
| `teaching` | Courses, curriculum, classroom practice, AI literacy, new programmes |
| `assessment` | Academic integrity, misconduct process, detection tools, disclosure of student use |
| `research` | Studies and findings, including AI's effect on research practice |
| `publishing` | Scholarly publishing, peer review, authorship and contribution disclosure |
| `funding` | Grants, awards, endowed chairs, institutional budgets |
| `workforce` | Hiring, faculty roles, staff training, labour effects |
| `tools` | Platforms, licensing deals, vendor offerings, procurement, industry moves |
| `safety` | Model safety and alignment, cyber security, privacy and data protection |
| `health` | Clinical and biomedical applications |

Adding a tag means editing `tag_vocabulary` in `_config.yml` as well as this file.
A tag used in an item but missing from the config is reported at the foot of
the topics page, so drift is visible rather than silent.

## Review rule

After about thirty briefings: merge any tag used fewer than three times;
split or drop any tag appearing on more than seven items in ten.

## Sections

Written as `section:` in each item; defined in `_config.yml`.

`canada` · `international` · `government` · `other`

An item whose section is not in that list appears under an "Unfiled" heading
at the foot of its briefing rather than vanishing.
