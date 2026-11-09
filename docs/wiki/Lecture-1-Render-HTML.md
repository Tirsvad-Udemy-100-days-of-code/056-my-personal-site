**English** · [Dansk](Lecture-1-Render-HTML-da) · [Bahasa Malaysia](Lecture-1-Render-HTML-ms)

# Lecture 1: Render HTML

**Goal:** serve a real HTML page with Flask instead of a plain string.

![Lecture 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/raw/branch/main/docs/screenshots/lecture-1-render-html.png)

## Steps

1. Create the server: import `Flask`, create `app = Flask(__name__)` and add the home route with `@app.route("/")`. First it returns the string `Hello, World!`.
2. Create `index.html` with the HTML boilerplate, a `title` and an `h1`.
3. Put the file in a folder called `templates`. Flask looks for HTML only there.
4. Import `render_template` and return `render_template("index.html")`.
5. Run in debug mode so the server reloads when you save.

## What we gained

- How a route connects a URL to a Python function.
- Why HTML belongs in the `templates` folder and what `render_template` does.
- Debug mode for a fast feedback loop.
- How to test a page without a browser: the Flask test client checks the status code and the heading (`tests/integration/test_home_route.py`).
