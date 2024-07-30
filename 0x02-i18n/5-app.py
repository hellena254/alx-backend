#!/usr/bin/env python3
"""
Flask app with Babel configuration for internationalization, locale selection,
and user emulation.
"""

from flask import Flask, render_template, request, g
from flask_babelex import Babel, gettext as _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """
    Configuration class for the Flask app.
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
    Determine the best match for supported languages.
    If the `locale` parameter is present in the request and valid, use it.
    Returns:
        str: The best matched language code.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """
    Mock a user login system by checking the `login_as` URL parameter.
    Returns:
        dict: The user dictionary if found, otherwise None.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None

@app.before_request
def before_request():
    """
    Execute before each request. Set the logged-in user in the Flask global object.
    """
    g.user = get_user()

@app.route('/')
def index() -> str:
    """
    Renders the index page.
    Returns:
        str: The rendered template as a string.
    """
    return render_template('5-index.html', 
                           home_title=_("home_title"), 
                           home_header=_("home_header"),
                           logged_in_as=_("logged_in_as") % {'username': g.user['name']} if g.user else _("not_logged_in"))

if __name__ == '__main__':
    app.run(debug=True)

