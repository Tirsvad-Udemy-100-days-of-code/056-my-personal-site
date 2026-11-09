# Documentation, wiki and repository metadata

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude for S01 | AI as stand-in for S01 | Initial version | [d32718e] |

---

## Purpose

Decide whether the repository is ready to share: README complete, a wiki in three languages that explains what was gained in each lecture step, and a repository description with topics.

## Deliverable

A final README, a wiki under `docs/wiki/` in English, Danish and Bahasa Malaysia with the same page set and the three lecture screenshots, generated Doxygen output with no errors, and a repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `check-languages.sh` reports no finding and every English wiki page has a `-da` and a `-ms` twin | No finding, equal page sets | Any gap |
| 2 | Each lecture step has a wiki page that explains what was gained and shows its screenshot | 3 of 3 | Fewer |
| 3 | `check-readme.sh` reports no finding | No finding | Any finding |
| 4 | The repository description is set and at least five topics exist | Set | Missing |
| 5 | `doxygen Doxyfile` runs without errors or warnings about missing documentation | Clean | Errors |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | All three lecture steps and their screenshots must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4 (README and three-language wiki) | [BC-001] |
| CN-005, CN-007 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-13 — within the one-week window of the Business Case constraint (2026-11-09 to 2026-11-13).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the English wiki | Write the English wiki pages in `docs/wiki/`: Home, one page per lecture step with what was gained, the architecture, and running the project. Include the screenshots. English is the authoritative text. | No |  |
| 2 | Translate the wiki to Danish | Translate every English wiki page to Danish (`-da` files) with the language line and the same page set, as `framework/process/wiki.md` requires. | No |  |
| 3 | Translate the wiki to Bahasa Malaysia | Translate every English wiki page to Bahasa Malaysia (`-ms` files) with the same page set. | No |  |
| 4 | Finalise the README | Check the README against the template, link the wiki and the project documents, and keep the lecture screenshots. | No |  |
| 5 | Set repository description and topics | Set the description and topics of the repository on the git host with the API, using the token from `.env`, which is never printed or committed. | No |  |
| 6 | Generate Doxygen output | Run Doxygen over the source to prove the comments are valid, without committing the generated output. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[d32718e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/commit/d32718e43960fc70996a1bc58979d71aa42046ef
