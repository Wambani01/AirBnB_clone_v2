#!/usr/bin/python3
"""a script to return all states from db"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)

@app.teardown_appcontext
def clean_up(exception=None):
    """a function to release db resources"""
    
    storage.close()

@app.route("/states_list", strict_slashes=False)
def states_list():
    """a function to return all states from db"""

    states = storage.all(State)
    return render_template("7-states_list.html", states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
