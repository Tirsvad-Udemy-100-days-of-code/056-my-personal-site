**English** · [Dansk](Architecture-da) · [Bahasa Malaysia](Architecture-ms)

# Architecture

The code follows Clean Architecture. Dependencies point inward: `presentation` and `infrastructure` know `application` and `domain`, never the reverse.

| Layer | Holds | Knows |
| --- | --- | --- |
| `domain` | `Skill`, `Education`, `Project`, `Profile` and the rules of a skill | nothing |
| `application` | The `GetProfile` use case and the `ProfileRepository` port | `domain` |
| `infrastructure` | `InCodeProfileRepository`, the data of the site owner | `application`, `domain` |
| `presentation` | Flask: `server.py`, `templates/`, `static/` | all layers (composition root) |

## What we gained

- The assignment's names (`server.py`, `templates`, `static`, `render_template`) stay, so coursists can compare solutions.
- A port lets us swap the data source (for example a database) without touching the use case or the page.
- An architecture test (`tests/unit/test_layering.py`) fails if `domain` or `application` imports Flask.
- `constants.py` defines each constant once.
