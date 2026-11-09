# Lecture 2: static files and CSS

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude for S01 | AI as stand-in for S01 | Initial version | [d32718e] |

---

## Purpose

Decide whether lecture 2 is reproduced: static files (CSS, images) are served from the `static` folder and linked from the template.

## Deliverable

A `static/css/style.css` file that changes the page background colour, linked in the `head` of `index.html`, a test that proves the file is served, and the lecture 2 screenshot in the README.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `GET /static/css/style.css` returns HTTP 200 with the stylesheet | Yes | No |
| 2 | `index.html` links the stylesheet with `url_for("static", ...)` | Yes | No |
| 3 | `pytest` exits with code 0 | Exit 0 | Any failure |
| 4 | The lecture 2 screenshot exists and is shown in the README | Exists and shown | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The rendered page and the screenshot tooling must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 2 (static files, CSS background) | [BC-001] |
| CN-003, CN-004 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-11 — within the one-week window of the Business Case constraint (2026-11-09 to 2026-11-13).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add static folder and CSS file | Create `static/css/style.css` that changes the background colour. Static files live in a folder called `static`, next to `templates`. | No |  |
| 2 | Link the stylesheet in the template | Add a `link` element to the `head` of `index.html` using `url_for("static", filename="css/style.css")`, so the path stays correct if the folder moves. | No |  |
| 3 | Test that static files are served | Add a test that the stylesheet returns 200 with the CSS content type and that the template links it. | No |  |
| 4 | Capture lecture 2 screenshot and update README | Capture the page with the new background and add it to the README, with a note about browser caching of static files. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[d32718e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/commit/d32718e43960fc70996a1bc58979d71aa42046ef
