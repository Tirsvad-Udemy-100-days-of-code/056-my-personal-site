# SQA Review Record RC-014: SH-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [SH-001], [QC-SH-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Claude for S01 | AI as stand-in for S01 | Initial version | [29172f1] |

---

## Artifact Under Review

- Instance reviewed: [SH-001]
- Checklist used: [QC-SH-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none (the stand-in reads English and covers the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Starts with `#!/usr/bin/env bash` and `set -euo pipefail` (or a comment explains the exception) | Pass | Starts with `#!/usr/bin/env bash` and `set -euo pipefail`. |
| 2 | Every expansion is quoted; lists are arrays; tests use `[[ ]]` and `$(...)` | Pass | Every expansion is quoted; tests use `if` and `$(...)`. |
| 3 | Names follow the conventions: `kebab-case.sh` files, `snake_case` functions and variables, `UPPER_SNAKE` constants and environment variables | Pass | `take-screenshot.sh` is kebab-case; variables (`root_host`, `network`) are snake_case; the function `cleanup` is snake_case. |
| 4 | Passes `shellcheck` and `bash -n` with no unexplained `disable` comments | Pass | shellcheck 0.11.0 and `bash -n` (GNU bash 5.2.37) report nothing; no disable comments. |
| 5 | Errors go to standard error with an `error:` message and a non-zero exit code; bad or missing arguments print a usage line | Pass | A missing file name prints the usage line (`${1:?usage: ...}`); a start failure prints `error: the application did not start` to standard error and exits 1. |
| 6 | Temporary files use `mktemp` with a `trap ... EXIT` cleanup; no fixed `/tmp` names | N-A | The script uses no temporary files. |
| 7 | No secret is written in the script, echoed, or put on a command line; secrets come from the environment or a gitignored file | Pass | No secret is read, written or echoed. |
| 8 | A script that changes state outside its own directory defaults to a dry run or needs an explicit flag, and says so in its header | Pass | It writes only `docs/screenshots/` in the repository and its own Docker containers and network, which a trap removes; the header says so. |
| 9 | A header comment states purpose, usage, options, environment variables and exit codes | Pass | The header gives purpose, usage, example, output, needs and exit codes; there are no options and no environment variables. |
| 10 | The script implements a task or design it cites; deviations are recorded | Pass | Implements task MIL-002#4 (screenshot tooling in Docker) and the rule of `framework/process/gui-testing.md`. |
| 11 | Behaviour is tested for success, failure and any disabled or bypass path | Pass | Recorded manual runs: three screenshots written on success; with Docker stopped the run failed with a non-zero exit code. |
| 12 | Formatted with `shfmt` (or the project's formatter) | Pass | `shfmt` 3.14.1 reports no difference. |
| 13 | Safe to re-run: a second run does not duplicate or corrupt what the first did | Pass | A re-run removes a leftover container and network first (`cleanup`), then recreates them. |
| 14 | Bash version and external tools it needs are stated; GNU-only options are named | Pass | The header names Bash and Docker (images python:3.13-slim and zenika/alpine-chrome); `cygpath` is used only when present. |
| 15 | A command sequence, constant, path or message used more than once is defined once (a function, a variable or a sourced helper); a helper is shared between scripts only where it expresses the same knowledge | Pass | The cleanup commands and names are defined once. |

## Overall Verdict

Go — all mandatory criteria pass or are not applicable with a stated reason; no blocking finding. Stand-in decision for S01, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[SH-001]: ../../../scripts/take-screenshot.sh
[QC-SH-001]: ../../../framework/qc/code/qc-programming-shell.md
[29172f1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/commit/29172f16f756862323db521e16614441fbf334fa
