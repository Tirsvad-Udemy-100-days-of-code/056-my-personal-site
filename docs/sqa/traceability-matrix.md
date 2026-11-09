# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Claude for S01 | AI as stand-in for S01 | Added SH-001 and RC-014 | [29172f1] |
| 2026-11-09 | Accepted | Claude for S01 | AI as stand-in for S01 | WIKI-001 last reviewed in RC-015 | [a7433a4] |

---

## Purpose

Tracks backward and forward links between artifact instances so that traceability is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-003] |
| [MIL-001] | MIL | en | it | [PP-001] | [MIL-002] | [RC-004] |
| [MIL-002] | MIL | en | it | [MIL-001] | [MIL-003] | [RC-005] |
| [MIL-003] | MIL | en | it | [MIL-002] | [MIL-004] | [RC-006] |
| [MIL-004] | MIL | en | it | [MIL-003] | [MIL-005] | [RC-007] |
| [MIL-005] | MIL | en | it | [MIL-004] | - | [RC-008] |
| [PY-MIL-001] | PY | - | - | [MIL-001] | - | [RC-009] |
| [PY-MIL-002] | PY | - | - | [MIL-002] | - | [RC-010] |
| [PY-MIL-003] | PY | - | - | [MIL-003] | - | [RC-011] |
| [PY-MIL-004] | PY | - | - | [MIL-004] | - | [RC-012] |
| [WIKI-001] | WIKI | en, da, ms | - | [MIL-005] | - | [RC-015] |
| [SH-001] | SH | - | - | [MIL-002] | - | [RC-014] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-004] | - | - | Covered |
| CN-002 | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | - | - | Covered |
| CN-003 | [MIL-001], [MIL-002] | - | - | Covered |
| CN-004 | [MIL-002], [MIL-003], [MIL-004], [MIL-005] | - | - | Covered |
| CN-005 | [MIL-005] | - | - | Covered |
| CN-006 | [MIL-001] | - | - | Covered |
| CN-007 | [MIL-005] | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | - | None found | - | Closed | - |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-lecture-1-render-html.md
[MIL-003]: ../milestones/mil-003-lecture-2-static-files.md
[MIL-004]: ../milestones/mil-004-lecture-3-cv-site.md
[MIL-005]: ../milestones/mil-005-documentation-and-wiki.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[RC-007]: ./reviews/rc-007-mil-004.md
[RC-008]: ./reviews/rc-008-mil-005.md
[RC-009]: ./reviews/rc-009-py-mil-001.md
[PY-MIL-001]: ../../src/personal_site
[RC-010]: ./reviews/rc-010-py-mil-002.md
[PY-MIL-002]: ../../src/personal_site
[RC-011]: ./reviews/rc-011-py-mil-003.md
[PY-MIL-003]: ../../src/personal_site
[RC-012]: ./reviews/rc-012-py-mil-004.md
[PY-MIL-004]: ../../src/personal_site
[RC-013]: ./reviews/rc-013-wiki.md
[WIKI-001]: ../wiki
[RC-014]: ./reviews/rc-014-sh-screenshot.md
[RC-015]: ./reviews/rc-015-wiki-published.md
[SH-001]: ../../scripts/take-screenshot.sh
[29172f1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/commit/29172f16f756862323db521e16614441fbf334fa
[a7433a4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/commit/a7433a40de7119feff442970850ee3fe45ca604a
