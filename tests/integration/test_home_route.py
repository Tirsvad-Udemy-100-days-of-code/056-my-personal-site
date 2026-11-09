"""Integration tests for the home route and the CV page."""

import re

from flask.testing import FlaskClient

from personal_site.constants import PROFILE_PHOTO_PATH
from personal_site.presentation.server import create_app


def make_client() -> FlaskClient:
    return create_app().test_client()


def home_html() -> str:
    return make_client().get("/").get_data(as_text=True)


def test_home_returns_status_200() -> None:
    assert make_client().get("/").status_code == 200


def test_home_has_a_title_and_a_language() -> None:
    html = home_html()
    assert "<title>Jens Tirsvad Nielsen</title>" in html
    assert '<html lang="en">' in html


def test_home_shows_the_name_in_the_heading() -> None:
    assert "<h1>Jens Tirsvad Nielsen</h1>" in home_html()


def test_home_shows_the_skills_with_their_stars() -> None:
    html = home_html()
    assert "Software architecture" in html
    assert "Software SQA and QC" in html
    assert "AI for software development" in html
    assert 'aria-label="5 out of 5 stars">' + "⭐" * 5 in html
    assert 'aria-label="4 out of 5 stars">' + "⭐" * 4 in html


def test_home_mentions_linux_and_the_study() -> None:
    html = home_html()
    assert "Linux" in html
    assert "UCL" in html


def test_home_shows_the_photo() -> None:
    html = home_html()
    assert f'src="/static/{PROFILE_PHOTO_PATH}"' in html
    assert 'alt="Portrait of Jens Tirsvad Nielsen"' in html


def test_every_asset_path_of_the_page_resolves() -> None:
    client = make_client()
    html = client.get("/").get_data(as_text=True)
    assets = re.findall(r'(?:src|href)="(/static/[^"]+)"', html)
    assert assets
    for asset in assets:
        response = client.get(asset)
        assert response.status_code == 200, asset
        response.close()
