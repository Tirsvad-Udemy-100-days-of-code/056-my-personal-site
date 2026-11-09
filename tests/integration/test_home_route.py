"""Integration tests for the home route."""

from flask.testing import FlaskClient

from personal_site.presentation.server import create_app


def make_client() -> FlaskClient:
    return create_app().test_client()


def test_home_returns_status_200() -> None:
    assert make_client().get("/").status_code == 200


def test_home_says_hello_world() -> None:
    assert b"Hello, World!" in make_client().get("/").data
