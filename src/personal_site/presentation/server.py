"""Flask server of the personal site and its composition root.

@file
@brief Creates the Flask application, wires the layers and defines the home route.
"""

from flask import Flask, render_template

from personal_site.application.get_profile import GetProfile
from personal_site.application.ports import ProfileRepository
from personal_site.constants import (
    DEBUG_MODE,
    DEFAULT_HOST,
    DEFAULT_PORT,
    MAX_STARS,
    PROFILE_PHOTO_PATH,
    STATIC_FOLDER,
    STYLESHEET_PATH,
    TEMPLATES_FOLDER,
)
from personal_site.infrastructure.in_code_profile_repository import (
    InCodeProfileRepository,
)


def create_app(repository: ProfileRepository | None = None) -> Flask:
    """Create the Flask application.

    @brief Application factory and composition root.
    @param repository Source of the profile; the in-code data when omitted.
    @return The configured Flask application.
    """
    flask_app = Flask(
        __name__,
        template_folder=TEMPLATES_FOLDER,
        static_folder=STATIC_FOLDER,
    )
    get_profile = GetProfile(repository or InCodeProfileRepository())

    @flask_app.route("/")
    def home() -> str:
        """Render the CV home page.

        @brief Lecture 3: render the CV from the profile.
        @return The HTML of the home page.
        """
        return render_template(
            "index.html",
            profile=get_profile.execute(),
            max_stars=MAX_STARS,
            photo_path=PROFILE_PHOTO_PATH,
            stylesheet_path=STYLESHEET_PATH,
        )

    return flask_app


app = create_app()


def main() -> None:
    """Start the development server.

    @brief Entry point used by `python -m personal_site`.
    """
    app.run(host=DEFAULT_HOST, port=DEFAULT_PORT, debug=DEBUG_MODE)


if __name__ == "__main__":
    main()
