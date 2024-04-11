#!/usr/bin/env python3
"""Defining A Flask App"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Languages Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """gets the best language match"""
    # Locale from URL parameters
    locale_lang = request.args.get('locale')
    if locale_lang and locale_lang in Config.LANGUAGES:
        return locale_lang

    # Locale from user settings
    if hasattr(g, 'user') and g.user:
        users_lang = g.user.get('locale')
        if users_lang and users_lang in Config.LANGUAGES:
            return users_lang

    # Locale from request header

