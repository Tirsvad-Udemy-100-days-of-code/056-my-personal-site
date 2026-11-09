"""Flask server of the personal site (lecture 1: render HTML).

@file
@brief Creates the Flask application and defines the home route.
"""

from flask import Flask, render_template

from personal_site.constants import (
    DEBUG_MODE,
    DEFAULT_HOST,
    DEFAULT_PORT,
    STATIC_FOLDER,
    TEMPLATES_FOLDER,
)


def create_app() -> Flask:
    """Create the Flask application.

    @brief Application factory.
    @return The configured Flask application.
    """
    flask_app = Flask(
        __name__,
        template_folder=TEMPLATES_FOLDER,
        static_folder=STATIC_FOLDER,
    )

    @flask_app.route("/")
    def home() -> str:
        """Render the home page.

        @brief Lecture 1, step 2: render `templates/index.html`.
        @return The HTML of the home page.
        """
        return render_template("index.html")

    return flask_app


app = create_app()


def main() -> None:
    """Start the development server.

    @brief Entry point used by `python -m personal_site`.
    """
    app.run(host=DEFAULT_HOST, port=DEFAULT_PORT, debug=DEBUG_MODE)


if __name__ == "__main__":
    main()
