[English](Lecture-2-Static-Files) · **Dansk** · [Bahasa Malaysia](Lecture-2-Static-Files-ms)

# Lektion 2: Statiske filer

**Mål:** servere CSS og billeder og ændre sidens baggrund med dit eget stylesheet.

![Lektion 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/raw/branch/main/docs/screenshots/lecture-2-static-files.png)

## Trin

1. Opret en mappe, der hedder `static`, ved siden af `templates`, og læg `css/style.css` i den.
2. Skift baggrundsfarven i CSS-filen.
3. Link til filen i skabelonens `head` med `url_for('static', filename='css/style.css')`.
4. Genindlæs. Hvis intet ændrer sig, har browseren gemt den gamle fil i cachen: brug en hård genindlæsning (Ctrl+F5).

## Det fik vi ud af det

- Forskellen på skabeloner (som Flask gengiver) og statiske filer (som sendes uændret).
- `url_for` bygger den rigtige sti, så siden virker, selv om mappen flyttes.
- Browsere cacher statiske filer; en hård genindlæsning viser din seneste ændring.
- En test viser, at stylesheetet leveres som `text/css`.
