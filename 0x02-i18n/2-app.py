#/usr/bin/env python3

"""
Basic Flask app setup with babel configf for i18n
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class for the Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index page
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)
