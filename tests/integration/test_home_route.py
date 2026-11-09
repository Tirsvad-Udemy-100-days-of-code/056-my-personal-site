"""Integration tests for the home route."""

from flask.testing import FlaskClient

from personal_site.presentation.server import create_app


def make_client() -> FlaskClient:
    return create_app().test_client()


def test_home_returns_status_200() -> None:
    assert make_client().get("/").status_code == 200


def test_home_renders_the_index_template_heading() -> None:
    html = make_client().get("/").get_data(as_text=True)
    assert "<h1>Hi, I am Jens Tirsvad Nielsen</h1>" in html


def test_home_has_a_title_and_a_language() -> None:
    html = make_client().get("/").get_data(as_text=True)
    assert "<title>Jens Tirsvad Nielsen</title>" in html
    assert '<html lang="en">' in html
