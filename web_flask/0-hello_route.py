#!/usr/bin/python3
"""
starts an flask app
"""
from flask import Flask

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        return 'Hello HBNB!'

    app.run()
