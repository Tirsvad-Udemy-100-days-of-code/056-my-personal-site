**English** · [Dansk](Lecture-3-CV-Site-da) · [Bahasa Malaysia](Lecture-3-CV-Site-ms)

# Lecture 3: CV Site

**Goal:** turn a website template into your own personal CV site.

![Lecture 3](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-my-personal-site/raw/branch/main/docs/screenshots/lecture-3-cv-site.png)

## Steps

1. Get a free HTML and CSS template. The course zip link had expired, so the layout follows the course's public CV example; the HTML and CSS are written for this project.
2. Put the HTML in `templates/` and the CSS and images in `static/`, then fix every path with `url_for`.
3. Replace the example content with your own: name, photo, skills with stars, education, interests and projects.
4. Check every asset path in a test.

## What we gained

- How to organise a template into `templates` and `static`.
- Jinja: variables, loops and filters fill the page from data, so the content is not hard-coded in the HTML.
- Data and markup are separate: a `Profile` object holds the content, the template only shows it.
- Accessibility basics: `alt` text for the photo and an `aria-label` on the stars.
- Respecting licences and giving credit when you reuse a template.
- Privacy: the photo has its metadata removed before it is published.
