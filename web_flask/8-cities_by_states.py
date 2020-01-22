#!/usr/bin/python3
"""
list of City objects linked to the State
"""
from flask import Flask, render_template
from models import storage


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/cities_by_states', strict_slashes=False)
    def get_citiesbystates():
        states = storage.all('State')
        statel = []
        for key, state in states.items():
            statel.append(state)
        sortstatel = sorted(statel, key=lambda i: i.name)
        return render_template('8-cities_by_states.html', **locals())

    @app.teardown_appcontext
    def teardown_citiesbystates(e):
        storage.close()

    app.run()
