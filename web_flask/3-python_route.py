#!/usr/bin/python3
"""generate a flask script for python route"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """return Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    """retun C <text>"""
    text_with_spaces = text.replace('_', ' ')
    return f'C {(text_with_spaces)}'


@app.route("/python/", strict_slashes=False,
           defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def PYTHON_text(text):
    """return Python <text>"""
    text_with_spaces = text.replace('_', ' ')
    return f'Python {(text_with_spaces)}'


if __name__ == '__main__':
    """run the application on 0.0.0.0, port 500"""
    app.run(host='0.0.0.0', port=5000)
