#!/usr/bin/python3
"""
variable in url route with default value
"""
from flask import Flask


if __name__ == "__main__":

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        return "HBNB"

    @app.route('/c/<text>', strict_slashes=False)
    def ctext(text):
        text = text.replace('_', ' ')
        return "C %s" % text

    @app.route('/python', strict_slashes=False)
    @app.route('/python/<text>', strict_slashes=False)
    def pythontext(text="is cool"):
        text = text.replace("_", " ")
        return "Python %s" % text

    @app.route('/number/<int:n>', strict_slashes=False)
    def numbern(n):
        return "%s is a number" % n

    app.run()
