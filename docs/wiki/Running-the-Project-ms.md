[English](Running-the-Project) · [Dansk](Running-the-Project-da) · **Bahasa Malaysia**

# Menjalankan projek

Cipta dan gunakan `.venv` setempat:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

Jalankan dan uji:

```bash
python -m personal_site          # open http://127.0.0.1:5000/
python -m pytest
doxygen Doxyfile                 # source documentation in docs/doxygen/
bash scripts/take-screenshot.sh lecture-3-cv-site.png / 1000 1450
```

## Apa yang kami peroleh

- Persediaan yang boleh diulang: persekitaran maya mengasingkan pakej projek daripada sistem.
- Satu arahan untuk ujian dan satu untuk dokumentasi.
- Tangkapan skrin diambil dalam kontena Docker, jadi tiada tetingkap dibuka pada desktop anda.
