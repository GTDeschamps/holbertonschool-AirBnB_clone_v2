#!/usr/bin/python3
"""generate a flask script for generate a html page with number"""


from flask import Flask, render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def NUMBER(n):
    """ return the number"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ return template  html page number"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """run the application on 0.0.0.0, port 500"""
    app.run(host='0.0.0.0', port=5000)
