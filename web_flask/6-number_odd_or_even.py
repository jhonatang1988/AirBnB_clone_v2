#!/usr/bin/python3
"""
variable in url route with default value
"""
from flask import Flask, render_template


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

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def numbertemplaten(n):
        return render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def numberoddevenn(n):
        str = "even"
        return render_template('6-number_odd_or_even.html', **locals())

    app.run()
