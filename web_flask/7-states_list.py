#!/usr/bin/python3
"""generate a flask script for State_list"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display HTML page: (inside the tag BODY)"""
    state_list = storage.all(State).values()

    return render_template('7-states_list.html', all_states=state_list)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    """storage.close()"""
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
