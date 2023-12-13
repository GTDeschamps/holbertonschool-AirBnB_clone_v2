#!/usr/bin/python3
"""generate a flask script for State_list"""


from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)

    return render_template('states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
