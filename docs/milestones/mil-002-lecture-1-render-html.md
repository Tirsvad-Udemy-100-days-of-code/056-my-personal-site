# Lecture 1: render HTML with Flask

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude for S01 | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether lecture 1 is reproduced: a Flask server that first returns a string and then renders `index.html` from the `templates` folder with `render_template`.

## Deliverable

A running Flask application with the route `/` that renders `templates/index.html` (title and an `h1` with a personal message), tests for it, the screenshot tooling in a Docker container, and the lecture 1 screenshot in the README.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `GET /` returns HTTP 200 with the `h1` text of `index.html` | Both true | Either false |
| 2 | `index.html` is served from the `templates` folder with `render_template` | Yes | No |
| 3 | `pytest` exits with code 0 | Exit 0 | Any failure |
| 4 | The lecture 1 screenshot exists under `docs/screenshots/` and is shown in the README | Exists and shown | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The skeleton, configuration and test setup must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 (render `index.html` with `render_template`) | [BC-001] |
| CN-003, CN-004 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-10 — within the one-week window of the Business Case constraint (2026-11-09 to 2026-11-13).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create Flask server with Hello World route | Create the Flask application in `presentation/server.py` with the home route `/` returning a Hello World string, as the first step of lecture 1. This is the base that the following tasks turn into a rendered page. | No |  |
| 2 | Render index.html with render_template | Replace the string with `render_template("index.html")` and add `templates/index.html` with boilerplate, a title and an `h1` with a personal message. HTML must be in a folder called `templates`. | No |  |
| 3 | Test the home route | Add pytest tests with the Flask test client for status 200 and for the `h1` text, so the lecture result is proven without a browser. | No |  |
| 4 | Add screenshot tooling in Docker | Add a script that runs headless Chromium in a Docker container and writes a PNG to `docs/screenshots/`. The rule in `framework/process/gui-testing.md` forbids testing a GUI on the host desktop. | No |  |
| 5 | Capture lecture 1 screenshot and update README | Run the tooling, store the lecture 1 screenshot and show it in the README with a short run instruction. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
