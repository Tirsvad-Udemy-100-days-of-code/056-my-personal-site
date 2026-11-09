[English](Architecture) · **Dansk** · [Bahasa Malaysia](Architecture-ms)

# Arkitektur

Koden følger Clean Architecture. Afhængighederne peger indad: `presentation` og `infrastructure` kender `application` og `domain`, aldrig omvendt.

| Lag | Indeholder | Kender |
| --- | --- | --- |
| `domain` | `Skill`, `Education`, `Project`, `Profile` og reglerne for en færdighed | intet |
| `application` | Use casen `GetProfile` og porten `ProfileRepository` | `domain` |
| `infrastructure` | `InCodeProfileRepository`, sidens ejers data | `application`, `domain` |
| `presentation` | Flask: `server.py`, `templates/`, `static/` | alle lag (composition root) |

## Det fik vi ud af det

- Opgavens navne (`server.py`, `templates`, `static`, `render_template`) bevares, så kursister kan sammenligne løsninger.
- En port gør det muligt at skifte datakilde (for eksempel en database) uden at røre use casen eller siden.
- En arkitekturtest (`tests/unit/test_layering.py`) fejler, hvis `domain` eller `application` importerer Flask.
- `constants.py` definerer hver konstant ét sted.
