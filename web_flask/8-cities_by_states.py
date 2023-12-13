#!/usr/bin/python3
"""generate a flask script for Cities"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from markupsafe import escape


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display HTML page: (inside the tag BODY)"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template('7-states_list.html', states=sorted_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
