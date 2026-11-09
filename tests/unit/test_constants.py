"""Smoke test: the package imports and its constants are readable."""

from personal_site import __version__, constants


def test_version_is_a_non_empty_string() -> None:
    assert __version__


def test_flask_folder_names_follow_the_convention() -> None:
    assert constants.TEMPLATES_FOLDER == "templates"
    assert constants.STATIC_FOLDER == "static"


def test_default_port_is_a_valid_tcp_port() -> None:
    assert 1 <= constants.DEFAULT_PORT <= 65535
