#!/usr/bin/python3
"""Renders states HTML"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def end_db(exception):
    """Remove current section"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display all states"""
    states = storage.all(State)
    state_list = list(states.values())
    return render_template('7-states_list.html', states=state_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
