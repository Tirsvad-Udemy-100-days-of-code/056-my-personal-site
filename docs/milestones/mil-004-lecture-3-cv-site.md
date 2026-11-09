# Lecture 3: personal CV site from a template

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude for S01 | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether lecture 3 is reproduced: a free CV template is organised into `templates` and `static`, its paths are adjusted, and it is filled with the participant's own content.

## Deliverable

A personal CV site on `/` with the participant's name, photo, skills (Software architecture 5 stars, Software SQA and QC 5 stars, AI for software development 4 stars), a Linux and Datamatiker (UCL Odense) background, built on the layered code (profile entity, use case, repository, Flask view), tests, and the lecture 3 screenshot in the README.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `GET /` shows the name "Jens Tirsvad Nielsen", the three skills with their star ratings, and the photo | All shown | Any missing |
| 2 | All asset paths in the template resolve with HTTP 200 | All resolve | Any 404 |
| 3 | Domain and application layers import no Flask code | No Flask import | Flask import found |
| 4 | `pytest` exits with code 0 | Exit 0 | Any failure |
| 5 | The lecture 3 screenshot exists and is shown in the README | Exists and shown | Missing |
| 6 | The template origin and licence are named in the README | Named | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Static file serving and the stylesheet link must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3 (personal CV site) | [BC-001] |
| CN-001, CN-004 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — within the one-week window of the Business Case constraint (2026-11-09 to 2026-11-13).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Obtain the CV template and the photo | Download the course CV template zip (fall back to the public demo page if the link has expired), and copy the participant's photo into `static/images/`. Stop and report if no copy of the template can be had. | No |  |
| 2 | Model the profile in the domain layer | Add frozen dataclasses `Skill` and `Profile` in `domain`, a `ProfileRepository` port and a `GetProfile` use case in `application`, so the content is data and not hard-coded markup. | No |  |
| 3 | Provide the profile data in infrastructure | Add an in-code repository holding the participant's name, skills, Linux interest and Datamatiker study at UCL Odense, with added background content. | No |  |
| 4 | Adapt the template to Flask | Move `index.html` to `templates`, assets to `static`, adjust the paths with `url_for`, and render the profile with Jinja. Keep the template attribution. | No |  |
| 5 | Test the CV site | Add unit tests for the domain and the use case and integration tests with the Flask client for the rendered page and every asset path. | No |  |
| 6 | Capture lecture 3 screenshot and update README | Capture the final site, show it in the README and name the template origin and licence. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
