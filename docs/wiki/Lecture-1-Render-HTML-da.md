[English](Lecture-1-Render-HTML) · **Dansk** · [Bahasa Malaysia](Lecture-1-Render-HTML-ms)

# Lektion 1: Vis HTML

**Mål:** servere en rigtig HTML-side med Flask i stedet for en almindelig tekststreng.

![Lektion 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/raw/branch/main/docs/screenshots/lecture-1-render-html.png)

## Trin

1. Opret serveren: importér `Flask`, opret `app = Flask(__name__)` og tilføj hjemmeruten med `@app.route("/")`. Først returnerer den teksten `Hello, World!`.
2. Opret `index.html` med HTML-skelettet, en `title` og en `h1`.
3. Læg filen i en mappe, der hedder `templates`. Flask leder kun efter HTML dér.
4. Importér `render_template` og returnér `render_template("index.html")`.
5. Kør i debug-tilstand, så serveren genindlæses, når du gemmer.

## Det fik vi ud af det

- Hvordan en rute forbinder en URL med en Python-funktion.
- Hvorfor HTML hører hjemme i mappen `templates`, og hvad `render_template` gør.
- Debug-tilstand giver hurtig feedback.
- Hvordan man tester en side uden browser: Flasks testklient kontrollerer statuskoden og overskriften (`tests/integration/test_home_route.py`).
