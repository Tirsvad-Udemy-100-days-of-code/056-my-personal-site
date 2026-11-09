"""Flask server of the personal site (lecture 1: Hello World).

@file
@brief Creates the Flask application and defines the home route.
"""

from flask import Flask

from personal_site.constants import DEBUG_MODE, DEFAULT_HOST, DEFAULT_PORT


def create_app() -> Flask:
    """Create the Flask application.

    @brief Application factory.
    @return The configured Flask application.
    """
    flask_app = Flask(__name__)

    @flask_app.route("/")
    def home() -> str:
        """Answer the home route with a plain string.

        @brief Lecture 1, step 1: the Hello World route.
        @return The text shown in the browser.
        """
        return "Hello, World!"

    return flask_app


app = create_app()


def main() -> None:
    """Start the development server.

    @brief Entry point used by `python -m personal_site`.
    """
    app.run(host=DEFAULT_HOST, port=DEFAULT_PORT, debug=DEBUG_MODE)


if __name__ == "__main__":
    main()
