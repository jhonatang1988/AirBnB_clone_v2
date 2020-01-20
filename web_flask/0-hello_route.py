#!/usr/bin/python3
"""
starts an flask app
"""
from flask import Flask

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/')
    def index():
        app.strict_slashes = False
        return 'Hello HBNB!'

    app.run()
