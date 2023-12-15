#!/usr/bin/python3
"""generate a flask script for Cities"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display cities_by_states"""
    state_list = storage.all(State).values()

    return render_template('8-cities_by_states.html', all_states=state_list)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
