#!/usr/bin/python3
"""
deploys a second url route
"""
from flask import Flask


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/')
    def index():
        app.strict_slashes = False
        return 'Hello HBNB!'

    @app.route('/hbnb')
    def hbnb():
        app.strict_slashes = False
        return 'HBNB'

    app.run()
