#!/usr/bin/python3
"""
list states from database or filestorage in a route with flask
"""
from flask import Flask, render_template
from models import storage


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/hbnb', strict_slashes=False)
    def get_hbnb():
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

        places = storage.all('Place')
        placel = []

        for key, place in places.items():
            placel.append(place)

        sortplacel = sorted(placel, key=lambda i: i.name)

        users = storage.all('User')
        userl = []

        for key, user in users.items():
            userl.append(user)

        return render_template('100-hbnb.html', **locals())

    @app.teardown_appcontext
    def teardown_hbnb(e):
        storage.close()

    app.run(host="0.0.0.0", port=5000)
