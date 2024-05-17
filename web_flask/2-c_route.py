#!/usr/bin/python3
"""Start a Flask Web app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    """Route to display"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_bnb():
    """Route to display /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Routes C followed by text variable"""
    parsed_text = text.replace('_', ' ')
    return "C {}".format(parsed_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
