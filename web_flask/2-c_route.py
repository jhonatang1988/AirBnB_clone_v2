#!/usr/bin/python3
"""
variables in the url route
"""
from flask import Flask


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        return 'Hello HBNB!'

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        return 'HBNB'

    @app.route('/c/<text>', strict_slashes=False)
    def ctext(text):
        text = text.replace('_', ' ')
        return "C %s" % text

    app.run()
