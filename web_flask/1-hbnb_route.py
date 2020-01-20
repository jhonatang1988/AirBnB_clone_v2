#!/usr/bin/python3
"""
deploys a second url route
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

    app.run()
