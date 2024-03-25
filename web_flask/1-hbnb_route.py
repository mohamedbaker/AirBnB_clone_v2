#!/usr/bin/python3
"""Starts a Flask web application.
That listens on host 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: display “HBNB”
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'Hello HBNB!'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
