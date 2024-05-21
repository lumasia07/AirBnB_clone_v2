#!/usr/bin/python3
"""Renders states HTML"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def end_db(exception):
    """Remove current section"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """HBNB filters"""
    state = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', state=list(state.values()),
                           amenities=list(amenities.values()))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
