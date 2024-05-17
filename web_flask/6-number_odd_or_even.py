#!/usr/bin/python3
"""Start a Flask Web app"""

from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def default_text(text='is cool'):
    parsed_text = text.replace('_', ' ')
    return "Python {}".format(parsed_text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    """Display HTML page if n is a number"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_odd_or_even(n):
    """Number odd or even"""
    if n % 2 == 0:
        codition = 'even'
    else:
        condition = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, condition=condition)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
