**English** · [Dansk](Running-the-Project-da) · [Bahasa Malaysia](Running-the-Project-ms)

# Running the Project

Create and use a local `.venv`:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

Run and test:

```bash
python -m personal_site          # open http://127.0.0.1:5000/
python -m pytest
doxygen Doxyfile                 # source documentation in docs/doxygen/
bash scripts/take-screenshot.sh lecture-3-cv-site.png / 1000 1450
```

## What we gained

- A reproducible set-up: a virtual environment keeps the project's packages apart from the system.
- One command for the tests, one for the documentation.
- Screenshots taken in a Docker container, so no window opens on your desktop.
