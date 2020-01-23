#!/usr/bin/python3
"""
list states from database or filestorage in a route with flask
"""
from flask import Flask, render_template
from models import storage


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/hbnb_filters', strict_slashes=False)
    def get_filters():
        states = storage.all('State')
        statel = []
        for key, state in states.items():
            statel.append(state)
        sortstatel = sorted(statel, key=lambda i: i.name)

        amenities = storage.all('Amenity')
        amenityl = []

        for key, amenity in amenities.items():
            amenityl.append(amenity)

        sortamenityl = sorted(amenityl, key=lambda i: i.name)

        return render_template('10-hbnb_filters.html', **locals())

    @app.teardown_appcontext
    def teardown_filters(e):
        storage.close()

    app.run(host="0.0.0.0", port=5000)
