# Project setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude for S01 | AI as stand-in for S01 | Initial version | [d32718e] |

---

## Purpose

Decide whether the project skeleton is sound enough to build the lecture steps on: configuration, folder structure, tooling and instructions.

## Deliverable

A repository skeleton with `pyproject.toml` (Python 3.13 or later, Flask as the only runtime dependency, pytest as test extra), a Python `.gitignore`, the layered package under `src/personal_site/`, `constants.py`, a Doxyfile, a README from the framework template with the `.venv` instructions, and a passing smoke test.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e .[test]` succeeds in a fresh `.venv` on Python 3.13 or later | Succeeds | Fails |
| 2 | `pytest` exits with code 0 | Exit 0 | Any failure |
| 3 | `pyproject.toml` lists Flask as the only runtime dependency | One dependency | More than one |
| 4 | `doxygen Doxyfile` runs without errors | No errors | Errors |
| 5 | README has every section of the framework README template and passes `check-readme.sh` | Passes | Fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First milestone after the baseline documents |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5 (Flask only, Python 3.13, `.venv`) | [BC-001] |
| CN-003, CN-006 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-09 — within the one-week window of the Business Case constraint (2026-11-09 to 2026-11-13).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Configure pyproject.toml | Create `pyproject.toml` with `requires-python >= 3.13`, Flask as the only runtime dependency, a `test` extra with pytest, and pytest settings. S02 and S03 need a project that installs with one command and has no extra runtime dependencies. | No |  |
| 2 | Add Python .gitignore | Add a Python `.gitignore` that also ignores `.env`, `.venv` and `/docs/ai-prompts/`, because the repository is public and the `.env` holds personal tokens. | No |  |
| 3 | Create layered package skeleton and constants.py | Create `src/personal_site/` with `domain`, `application`, `infrastructure` and `presentation` packages and a `constants.py` holding every constant, as the clean-architecture folder structure asks. Add `tests/unit`, `tests/integration` and `tests/e2e`. | No |  |
| 4 | Add Doxyfile | Add a `Doxyfile` configured for Python (`OPTIMIZE_OUTPUT_JAVA` off, `EXTRACT_ALL` on) so that the Doxygen comments in the source generate documentation without errors. | No |  |
| 5 | Write README with venv instructions | Write `README.md` from the framework template: how to create and use a local `.venv`, upgrade pip with `python -m pip install --upgrade pip`, install, run and test. | No |  |
| 6 | Add smoke test | Add a pytest smoke test that imports the package and reads a constant, so the test command is proven before real features arrive. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[d32718e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/commit/d32718e43960fc70996a1bc58979d71aa42046ef
