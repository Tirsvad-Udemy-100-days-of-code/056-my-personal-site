[English](Lecture-1-Render-HTML) · [Dansk](Lecture-1-Render-HTML-da) · **Bahasa Malaysia**

# Kuliah 1: Paparkan HTML

**Matlamat:** menghidangkan halaman HTML sebenar dengan Flask dan bukannya rentetan teks biasa.

![Kuliah 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/raw/branch/main/docs/screenshots/lecture-1-render-html.png)

## Langkah

1. Cipta pelayan: import `Flask`, cipta `app = Flask(__name__)` dan tambah laluan utama dengan `@app.route("/")`. Pada mulanya ia memulangkan teks `Hello, World!`.
2. Cipta `index.html` dengan rangka HTML, satu `title` dan satu `h1`.
3. Letakkan fail itu dalam folder bernama `templates`. Flask hanya mencari HTML di situ.
4. Import `render_template` dan pulangkan `render_template("index.html")`.
5. Jalankan dalam mod nyahpepijat supaya pelayan dimuat semula apabila anda menyimpan.

## Apa yang kami peroleh

- Bagaimana laluan (route) menghubungkan URL dengan fungsi Python.
- Mengapa HTML perlu berada dalam folder `templates` dan apa yang dilakukan oleh `render_template`.
- Mod nyahpepijat memberi maklum balas yang pantas.
- Cara menguji halaman tanpa pelayar: klien ujian Flask menyemak kod status dan tajuk (`tests/integration/test_home_route.py`).
