# Flask i18n Project

## Overview

This project demonstrates how to implement internationalization (i18n) and localization (l10n) in a Flask web application. It uses the Flask-Babel extension to support multiple languages and time zones, providing a seamless user experience for different locales.

## What is i18n?

Internationalization (i18n) is the process of designing a software application in such a way that it can be adapted to various languages and regions without engineering changes. This includes:
- **Text Translations**: Translating user interface elements and messages into different languages.
- **Locale-Specific Formats**: Adapting date, time, number, and currency formats according to the locale.
- **Cultural Sensitivity**: Considering cultural norms and practices in the application design.

## Flask and Flask-Babel

Flask is a lightweight WSGI web application framework in Python. Flask-Babel is an extension for Flask that adds i18n and l10n capabilities to Flask applications. It integrates with Flask to handle language translations and time zone conversions.

## Project Structure

- `0-app.py`: Basic Flask app with a single route displaying "Welcome to Holberton".
- `1-app.py`: Adds Flask-Babel configuration for i18n.
- `2-app.py`: Implements language selection based on URL parameters and request headers.
- `3-app.py`: Uses gettext for template translations and sets up Babel configuration.
- `4-app.py`: Allows forcing a locale through URL parameters.
- `5-app.py`: Mocks user login and displays messages based on user login status.
- `6-app.py`: Adds user-specific locale settings.
- `7-app.py`: Adds time zone support and displays current time based on inferred time zone.

## How to Run

1. **Install Dependencies**
    ```sh
    pip install flask==1.1.2 flask_babel==2.0.0 pytz
    ```

2. **Run the Application**
    ```sh
    ./7-app.py
    ```

3. **Access the Application**
    Visit `http://127.0.0.1:5000/` in your browser.

## Key Features

- **Language Selection**: Automatically detects and applies the best language based on URL parameters, user settings, or request headers.
- **Time Zone Handling**: Infers and applies the correct time zone, displaying the current time in the user's local time.
- **User Emulation**: Mocks a user login system to demonstrate personalized settings.
- **Translation Management**: Uses Babel to manage translations with `.po` and `.mo` files for different languages.

## Configuration Files

- `babel.cfg`: Configuration file for Babel to extract messages from Python and Jinja2 files.
- `translations/en/LC_MESSAGES/messages.po`: English translations.
- `translations/fr/LC_MESSAGES/messages.po`: French translations.
