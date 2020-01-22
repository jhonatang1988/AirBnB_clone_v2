#!/usr/bin/python3
"""
list states from database or filestorage in a route with flask
"""
from flask import Flask, render_template, g
from models import storage


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/states_list', strict_slashes=False)
    def get_stateslist():
        states = storage.all('State')
        statel = []
        for key, state in states.items():
            statel.append(state)
        sortstatel = sorted(statel, key=lambda i: i.name)
        return render_template('7-states_list.html', **locals())

    @app.teardown_appcontext
    def teardown_stateslist(e):
        storage.close()

    app.run()
