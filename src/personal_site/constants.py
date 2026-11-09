"""All constants of the personal site live here.

@file
@brief Single place for constants, so that each value is defined once.
"""

## @brief Name of the application, used in titles and logs.
APP_NAME: str = "personal-site"

## @brief Host the development server binds to.
DEFAULT_HOST: str = "127.0.0.1"

## @brief Port the development server listens on.
DEFAULT_PORT: int = 5000

## @brief Name of the folder that holds the HTML templates (Flask convention).
TEMPLATES_FOLDER: str = "templates"

## @brief Name of the folder that holds static files (Flask convention).
STATIC_FOLDER: str = "static"

## @brief Run the development server in debug mode (auto reload). Development only.
DEBUG_MODE: bool = True

## @brief Highest star rating a skill can have.
MAX_STARS: int = 5

## @brief Lowest star rating a skill can have.
MIN_STARS: int = 1

## @brief Path of the profile photo, relative to the static folder.
PROFILE_PHOTO_PATH: str = "images/jens.jpg"

## @brief Path of the stylesheet, relative to the static folder.
STYLESHEET_PATH: str = "css/style.css"
