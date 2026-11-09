**English** · [Dansk](Lecture-2-Static-Files-da) · [Bahasa Malaysia](Lecture-2-Static-Files-ms)

# Lecture 2: Static Files

**Goal:** serve CSS and images, and change the page background with your own stylesheet.

![Lecture 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/raw/branch/main/docs/screenshots/lecture-2-static-files.png)

## Steps

1. Create a folder called `static` next to `templates` and put `css/style.css` in it.
2. Change the background colour in the CSS.
3. Link the file in the `head` of the template with `url_for('static', filename='css/style.css')`.
4. Reload. If nothing changes, the browser has cached the old file: use a hard refresh (Ctrl+F5).

## What we gained

- The difference between templates (rendered by Flask) and static files (served as they are).
- `url_for` builds the right path, so the page keeps working if the folder moves.
- Browsers cache static files; a hard refresh shows your latest change.
- A test proves the stylesheet is served as `text/css`.
