#!/usr/bin/python3
"""generate the first flask script"""


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


if __name__ == '__main__':
    """run the application on 0.0.0.0, port 500"""
    app.run(host='0.0.0.0', port=5000)
