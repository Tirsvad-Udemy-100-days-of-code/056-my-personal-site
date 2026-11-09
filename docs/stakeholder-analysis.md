# Stakeholder Analysis: Personal Site

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude for S01 | AI as stand-in for S01 | Initial version | [d32718e] |

---

## Purpose

This analysis identifies who has influence over, or interest in, the personal site project, so that the Business Case, the plan and the reviews engage the right people with the right level of attention. It follows the power/interest grid and maps each concern to a FURPS+ attribute.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Self; Datamatiker student at UCL Odense | HIGH | HIGH | Manage Closely | A finished, personal and reviewed result of the Day 56 assignment |
| S02 | Udemy coursists | Fellow participants of the 100 Days of Code course | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's names, and instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear description, topics and README, and no runtime dependencies beyond Flask |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** S01 decides scope, owns the code and reviews the result. Both power and interest are high, so S01 is consulted on every decision and owns every milestone.
- **Keep Informed (S02):** Coursists cannot change the project, but they compare solutions and will copy the structure. They need current instructions and stable names.
- **Monitor (S03):** Viewers arrive occasionally and decide in seconds whether the repository is useful. They need no direct contact, only a clear first page.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The site must show my name, photo, skills and background as a Linux fan and Datamatiker student | Functionality |
| CN-002 | S01 | Every lecture step must be reviewed and documented before the next one | Supportability |
| CN-003 | S02 | The code must run with a few commands and use the assignment's file and function names | Usability |
| CN-004 | S02 | Each lecture step must be visible, with a screenshot and an explanation | Usability |
| CN-005 | S03 | The repository needs a clear description, topics and README | Usability |
| CN-006 | S03 | The project must not pull in runtime dependencies other than Flask | Supportability |
| CN-007 | S01 | The wiki must exist in English, Danish and Bahasa Malaysia | Usability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat with the AI assistant | At acceptance of the plan and at the final summary | Plan, final summary with review records and stand-in decisions | All milestones |
| S02 | README and wiki | Updated per lecture milestone | Run instructions and lecture explanations | MIL-002 to MIL-005 |
| S03 | Repository description, topics and README | Once, at the documentation milestone | Description, topics, README | MIL-005 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 wants the personal photo and information kept, while S02 and S03 read the public repository | S01, S02, S03 | Only the data S01 supplied is published; S01 can remove it by editing one data file and one image |
| S02 wants the assignment's plain structure, while the framework asks for layered Clean Architecture | S02, S01 | The assignment's names (`server.py`, `templates/`, `static/`, `render_template`) are kept; the layers are explained in the wiki |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | Objective 3 in [BC-001] |
| S01 | CN-002 | Objectives 1 to 3 in [BC-001] |
| S02 | CN-003 | Objectives 1 and 5 in [BC-001] |
| S02 | CN-004 | Objective 4 in [BC-001] |
| S03 | CN-005 | Objective 4 in [BC-001] |
| S03 | CN-006 | Objective 5 in [BC-001] |
| S01 | CN-007 | Objective 4 in [BC-001] |

## Sign-Off

Authored and reviewed in autonomous mode: the AI acts as stand-in for S01, not independent. S01 can challenge it in the final summary.

---

[BC-001]: ./business-case.md
[d32718e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/commit/d32718e43960fc70996a1bc58979d71aa42046ef
