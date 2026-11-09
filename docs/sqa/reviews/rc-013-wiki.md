# SQA Review Record RC-013: WIKI-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [WIKI-001], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Claude for S01 | AI as stand-in for S01 | Initial version | [21dcc9f] |

---

## Artifact Under Review

- Instance reviewed: [WIKI-001]
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: en, da, ms (wiki)
- Language reviewer: none (the stand-in reads English and covers the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | The sidebar starts with the bold title and one English page list, `Home` first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All six English pages are listed; every link points to an existing file. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | The wiki has no related wikis, so it has no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages is the last section, one line per language: English, Dansk, Bahasa Malaysia, each linking to its Home. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written by hand, not generated. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has a language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English is present; the PO language is English, so no further minimum. Danish (da) and Bahasa Malaysia (ms) are added on top. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Six English pages, six `-da` and six `-ms` pages: identical page sets. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Each page starts with a language line in the form `**English** · [Dansk](Page-da) · [Bahasa Malaysia](Page-ms)`, the current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Non-English pages are named `<Page>-da.md` and `<Page>-ms.md`; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Code blocks, commands and file names are English in every language. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | The wiki is published by the git host after the merge to main. The check on the published wiki is done after the merge and recorded in a delta re-review of criterion 14. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | No change to the layout rules. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | `docs/wiki/` is flat: every page and `_Sidebar.md` is directly in it; languages are told apart by file name. |

## Overall Verdict

Go-with-conditions — fifteen criteria pass or are not applicable; criterion 14 (check on the published wiki) is Pending until the merge. No blocking finding. Stand-in decision for S01, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the published wiki, its sidebar and every link, then re-review criterion 14 | S01 | 2026-11-13 |

---

[WIKI-001]: ../../wiki
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[21dcc9f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/commit/21dcc9f70e23f1573aeea2eac8c417e556855761
