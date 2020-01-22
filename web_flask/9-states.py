#!/usr/bin/python3
"""
list states from database or filestorage in a route with flask
"""
from flask import Flask, render_template, g
from models import storage


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/states', strict_slashes=False)
    @app.route('/states/<id>', strict_slashes=False)
    def get_states(id=""):
        states = storage.all('State')
        statel = []
        for key, state in states.items():
            statel.append(state)
        sortstatel = sorted(statel, key=lambda i: i.name)
        if id:
            for state in sortstatel:
                if state.id == id:
                    objfound = state
        return render_template('9-states.html', **locals())

    @app.teardown_appcontext
    def teardown_states(e):
        storage.close()

    app.run()
