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


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_and_states(id=None):
    """Display all states"""
    if id:
        id = 'State.{}'.format(id)
    return render_template('9-states.html', states=storage.all(State), id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
