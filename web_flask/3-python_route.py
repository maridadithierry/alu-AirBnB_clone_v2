#!/usr/bin/python3
""" Script that runs a flask application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ function that return " hello hbnb" """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ function that displays hbnb!"""
    return 'HBNB'

