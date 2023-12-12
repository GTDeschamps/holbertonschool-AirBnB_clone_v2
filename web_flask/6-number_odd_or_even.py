#!/usr/bin/python3

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_HBNB():
    return "<p>Hello HBNB!</p>"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "<p>HBNB</p>"

@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    text_with_spaces = text.replace('_', ' ')
    return f'C {(text_with_spaces)}'

@app.route("/python/", strict_slashes=False,
           defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def PYTHON_text(text):
    text_with_spaces = text.replace('_', ' ')
    return f'Python {(text_with_spaces)}'

@app.route("/number/<int:n>", strict_slashes=False)
def NUMBER(n):
    return f'{n} is a number'

from flask import Flask

app = Flask(__name__)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    odd_even = "odd" if n % 2 != 0 else "even"
    return render_template('6-number_odd_or_even.html',
                           n=n, odd_even=odd_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




