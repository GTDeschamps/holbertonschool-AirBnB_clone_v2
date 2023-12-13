#!/usr/bin/python3
"""generate a flask script for C route"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """return Hello HBNB"""
    return "<p>Hello HBNB!</p>"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """return HBNB"""
    return "<p>HBNB</p>"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    """retun C <text>"""
    text_with_spaces = text.replace('_', ' ')
    return f'C {(text_with_spaces)}'


if __name__ == '__main__':
    """run the application on 0.0.0.0, port 500"""
    app.run(host='0.0.0.0', port=5000)
