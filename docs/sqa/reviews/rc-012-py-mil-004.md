# SQA Review Record RC-012: PY-MIL-004

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [PY-MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Claude for S01 | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [PY-MIL-004]
- Checklist used: [QC-PY-001]
- Scope: full review of the domain, application, infrastructure and presentation code of the CV site (MIL-004)
- Language and domain: n/a (technical type)
- Language reviewer: none (the stand-in reads English and covers the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules and functions are snake_case, classes PascalCase, constants UPPER_SNAKE in domain/profile.py, application/get_profile.py, infrastructure and presentation/server.py. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (GetProfile, InCodeProfileRepository, MAX_STARS); no unexplained abbreviations. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check .` and `ruff check .` (rules E, F, I, B, UP, N, D) report nothing; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function signature is annotated, including `-> None`; `mypy --strict` agrees. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare `except`; no exception is swallowed. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default arguments; no builtin is shadowed. |
| 7 | Files, locks and connections are managed with context managers | Pass | No file or connection is opened by the code; nothing needs a context manager. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules, classes and functions have docstrings with Doxygen tags (@brief, @param, @return). |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging of secrets or personal data. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | This project has no Design Class Diagram; the tasks are technical tasks of the milestone and the layers are explained in the wiki. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | The 23 tests in tests/unit and tests/integration, including an architecture test of the layers are named for behaviour and independent of order and network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` runs on `src` without errors; no `Any` is used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Flask is the only runtime dependency; pytest, ruff and mypy are extras; none is unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Constants live once in `constants.py`; no knowledge is duplicated. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain and application import no Flask; imports point inward; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Each module has one reason to change; ports are narrow. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Source is in `domain`, `application`, `infrastructure` and `presentation` under `src/personal_site/`; tests in `unit`, `integration` and `e2e`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | File and folder names are English, lower case and contain only letters, digits, `_` and `.`. |

## Overall Verdict

Go — all mandatory criteria pass or are not applicable with a stated reason; no blocking finding. Stand-in decision for S01, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[PY-MIL-004]: ../../../src/personal_site
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
