#!/usr/bin/python3
"""Renders states HTML"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML for states in alphabetical order"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardoen_db(exception):
    """Closes current SQLAlchemy session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
