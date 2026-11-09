"""Integration tests for static files (lecture 2)."""

from flask.testing import FlaskClient

from personal_site.presentation.server import create_app

STYLESHEET_URL = "/static/css/style.css"


def make_client() -> FlaskClient:
    return create_app().test_client()


def test_stylesheet_is_served_as_css() -> None:
    response = make_client().get(STYLESHEET_URL)
    assert response.status_code == 200
    assert response.mimetype == "text/css"
    response.close()


def test_stylesheet_sets_a_background_colour() -> None:
    response = make_client().get(STYLESHEET_URL)
    assert "background-color" in response.get_data(as_text=True)
    response.close()


def test_home_links_the_stylesheet_from_the_static_folder() -> None:
    html = make_client().get("/").get_data(as_text=True)
    assert f'href="{STYLESHEET_URL}"' in html
