[English](Architecture) · [Dansk](Architecture-da) · **Bahasa Malaysia**

# Seni bina

Kod mengikut Clean Architecture. Kebergantungan menghala ke dalam: `presentation` dan `infrastructure` mengenali `application` dan `domain`, tidak sebaliknya.

| Lapisan | Mengandungi | Mengenali |
| --- | --- | --- |
| `domain` | `Skill`, `Education`, `Project`, `Profile` dan peraturan sesuatu kemahiran | tiada |
| `application` | Kes guna `GetProfile` dan port `ProfileRepository` | `domain` |
| `infrastructure` | `InCodeProfileRepository`, data pemilik laman | `application`, `domain` |
| `presentation` | Flask: `server.py`, `templates/`, `static/` | semua lapisan (composition root) |

## Apa yang kami peroleh

- Nama dalam tugasan (`server.py`, `templates`, `static`, `render_template`) dikekalkan, supaya peserta kursus dapat membandingkan penyelesaian.
- Port membolehkan sumber data ditukar (contohnya pangkalan data) tanpa mengubah kes guna atau halaman.
- Ujian seni bina (`tests/unit/test_layering.py`) gagal jika `domain` atau `application` mengimport Flask.
- `constants.py` mentakrifkan setiap pemalar di satu tempat sahaja.
