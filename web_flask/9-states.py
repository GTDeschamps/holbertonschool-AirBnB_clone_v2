#!/usr/bin/python3
"""generate a flask script for State"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_states():
    """display states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('states.html', states=sorted_states)


@app.route('/states/<state_id>', strict_slashes=False)
def display_state_cities(state_id):
    """display state_cities"""
    state = storage.get(State, state_id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('state_cities.html', state=state, cities=cities)
    else:
        return render_template('not_found.html')


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    """run the application on 0.0.0.0, port 500"""
    app.run(host='0.0.0.0', port=5000)
