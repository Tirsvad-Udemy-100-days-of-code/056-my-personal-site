[English](Lecture-3-CV-Site) · **Dansk** · [Bahasa Malaysia](Lecture-3-CV-Site-ms)

# Lektion 3: CV-siden

**Mål:** forvandle en hjemmesideskabelon til din egen personlige CV-side.

![Lektion 3](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/raw/branch/main/docs/screenshots/lecture-3-cv-site.png)

## Trin

1. Find en gratis HTML- og CSS-skabelon. Kursets zip-link var udløbet, så layoutet følger kursets offentlige CV-eksempel; HTML og CSS er skrevet til dette projekt.
2. Læg HTML i `templates/` og CSS og billeder i `static/`, og ret alle stier med `url_for`.
3. Erstat eksempelindholdet med dit eget: navn, foto, færdigheder med stjerner, uddannelse, interesser og projekter.
4. Kontrollér hver sti til en ressource i en test.

## Det fik vi ud af det

- Hvordan man organiserer en skabelon i `templates` og `static`.
- Jinja: variabler og løkker fylder siden ud fra data, så indholdet ikke er hårdkodet i HTML.
- Data og markup er adskilt: et `Profile`-objekt rummer indholdet, og skabelonen viser det blot.
- Grundlæggende tilgængelighed: `alt`-tekst til fotoet og `aria-label` på stjernerne.
- At respektere licenser og kreditere kilden, når man genbruger en skabelon.
- Privatliv: fotoets metadata er fjernet, før det offentliggøres.
