# Business Case: Personal Site

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude for S01 | AI as stand-in for S01 | Initial version | pending |

---

## Executive Summary

Jens Tirsvad Nielsen follows the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp". Day 56 asks the participant to serve HTML, CSS and images with Flask. This project delivers that assignment as a runnable, documented repository: a personal CV website for a Linux enthusiast and Datamatiker student at UCL Odense, built in three lecture steps (render HTML, serve static files, adopt a free CV template). The repository doubles as a reference for fellow course participants and as a portfolio piece for visitors on GitHub.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/`: artifacts are reviewed against the QC checklists before code is written, and quality is expressed in the ISO/IEC 25010:2023 characteristics. Software structure follows Clean Architecture; Python code follows PEP 8, PEP 257 and PEP 484 and is reviewed against `QC-PY-001`.

## Problem Statement

A course participant who only follows the video has no durable, reviewed result, and other participants cannot compare solutions. A bare solution folder without instructions, tests or screenshots is hard for a visitor to run or to learn from. The assignment also names its functions and files (`server.py`, `templates/`, `static/`), so a repository that departs from those names is harder to compare.

## Business Opportunity

A small, well-documented repository can show each lecture step with a screenshot, explain what was learned in three languages (English, Danish, Bahasa Malaysia), and give visitors a working personal site. This demonstrates the participant's skills in software architecture, SQA and QC, and AI for software development.

## Objectives

1. Deliver a Flask application that renders `index.html` from `templates/` with `render_template` on the route `/` (lecture 1).
2. Serve static assets (CSS, images) from `static/` and change the page background with a self-written CSS file (lecture 2).
3. Deliver a personal CV site, adapted from the free CV template of the course, that shows the participant's name, photo, skills and background (lecture 3).
4. Publish a README and a three-language wiki with one screenshot per lecture step and an explanation of what was gained in each step.
5. Keep the runtime dependency list to Flask only, and keep the code runnable on Python 3.13 or later with a local `.venv`.

## Scope

### In Scope

- Flask application in `src/`, tests with pytest in `tests/`, constants in `constants.py`.
- Templates and static files for the three lecture steps, including the participant's photo and personal information.
- `pyproject.toml`, Python `.gitignore`, Doxyfile and Doxygen comments, README from the framework template.
- Wiki in English, Danish and Bahasa Malaysia; screenshots taken in a headless browser in a Docker container.
- Repository description and topics on the git host.

### Out of Scope

- The sibling project 056-name-card (html5up Identity name card), which has its own repository and plan.
- A database, user accounts, a contact form or any server-side state.
- Hosting or deploying the site on a public server.

## Expected Benefits

### Tangible Benefits

- A runnable repository with passing tests that a coursist can start in three commands.
- At least one screenshot per lecture step (three or more), in the README and the wiki.
- A wiki in three languages that records what each step taught.

### Intangible Benefits

- A reviewed example of the framework applied to a small course project.
- A personal presentation page that can be reused as a portfolio.

## Strategic Alignment

The project supports the participant's learning goal of finishing the 100 Days of Code course and the study goal of practising software architecture, SQA and QC, and AI-assisted development in a documented way.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Test suite passes | 100 percent of tests pass on Python 3.13 | `pytest` exit code 0 |
| 2 | Lecture steps documented | 3 of 3 lecture steps have a screenshot in README and wiki | Count of screenshot files referenced |
| 3 | Wiki languages complete | 3 of 3 languages (en, da, ms) have the same page set | `check-languages.sh` and page list comparison |
| 4 | Runtime dependencies | Exactly 1 (Flask) | `[project] dependencies` in `pyproject.toml` |
| 5 | Milestones delivered | 5 of 5 milestones merged with a Go review | Merged pull requests and `RC-*` records |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The course template download link has expired | The CV template cannot be fetched | Fall back to the public demo page `angelabauer.github.io/cv`, and stop and report if no copy is available |
| Personal photo and information are published in a public repository | Privacy exposure | The Product Owner (S01) asked to keep the photo and information; only data given in the request is used |
| Screenshot tooling needs a browser | Screenshots cannot be produced | Use a headless browser in a Docker container, as `gui-testing.md` requires |
| Reviews are done by a stand-in, not an independent person | Lower assurance | Record the review as autonomous and not independent; S01 can challenge it in the final summary |

## Assumptions

- S01 is the Product Owner, developer and reviewer, and is reachable only through the chat.
- Docker, Python 3.13 and Git are available on the development machine.
- The CV template of the course allows reuse for learning purposes.

## Constraints

- Python 3.13 or later; `venv` for the virtual environment; pytest for tests; `constants.py` for constants.
- Source in `src/`, tests in `tests/`, documents in `docs/`.
- The planned duration is one week, from 2026-11-09 to 2026-11-13.
- No runtime dependency other than Flask.

## Cost–Benefit Assessment

The assessment is qualitative because the project is a learning exercise with no revenue; a monetary figure would be invented.

| Costs | Benefits |
| --- | --- |
| About one working week of the participant's time, guided by an AI assistant | A reviewed reference solution, a portfolio page and a documented learning record |
| Review effort by a stand-in reviewer | Reusable pattern for the later course projects |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Finish the assignment with a reviewed, personal result |
| S02 | Readable, runnable code with the assignment's names, and run instructions |
| S03 | A clear description, topics and README, with no runtime dependencies beyond Flask |

## Recommendation

Proceed — the scope is small, the risks are mitigated, and the result serves the participant, fellow coursists and repository visitors.

---

[SA-001]: ./stakeholder-analysis.md
