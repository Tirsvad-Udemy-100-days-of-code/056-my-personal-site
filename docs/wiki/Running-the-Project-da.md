[English](Running-the-Project) · **Dansk** · [Bahasa Malaysia](Running-the-Project-ms)

# Kør projektet

Opret og brug et lokalt `.venv`:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

Kør og test:

```bash
python -m personal_site          # open http://127.0.0.1:5000/
python -m pytest
doxygen Doxyfile                 # source documentation in docs/doxygen/
bash scripts/take-screenshot.sh lecture-3-cv-site.png / 1000 1450
```

## Det fik vi ud af det

- En reproducerbar opsætning: et virtuelt miljø holder projektets pakker adskilt fra systemets.
- Én kommando til testene og én til dokumentationen.
- Skærmbilleder taget i en Docker-container, så der ikke åbnes noget vindue på din skærm.
