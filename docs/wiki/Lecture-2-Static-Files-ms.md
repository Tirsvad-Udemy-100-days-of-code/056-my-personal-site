[English](Lecture-2-Static-Files) · [Dansk](Lecture-2-Static-Files-da) · **Bahasa Malaysia**

# Kuliah 2: Fail statik

**Matlamat:** menghidangkan CSS dan imej, dan menukar latar belakang halaman dengan helaian gaya anda sendiri.

![Kuliah 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/raw/branch/main/docs/screenshots/lecture-2-static-files.png)

## Langkah

1. Cipta folder bernama `static` di sebelah `templates` dan letakkan `css/style.css` di dalamnya.
2. Tukar warna latar belakang dalam fail CSS.
3. Pautkan fail itu dalam `head` templat dengan `url_for('static', filename='css/style.css')`.
4. Muat semula. Jika tiada perubahan, pelayar telah menyimpan fail lama dalam cache: gunakan muat semula penuh (Ctrl+F5).

## Apa yang kami peroleh

- Perbezaan antara templat (dipaparkan oleh Flask) dan fail statik (dihidangkan seperti sedia ada).
- `url_for` membina laluan yang betul, jadi halaman tetap berfungsi jika folder dipindahkan.
- Pelayar menyimpan fail statik dalam cache; muat semula penuh menunjukkan perubahan terkini anda.
- Satu ujian membuktikan helaian gaya dihidangkan sebagai `text/css`.
