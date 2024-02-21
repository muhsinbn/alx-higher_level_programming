#!/usr/bin/python3
"""defines a function that creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """loads the object from a json file"""
    with open(filename, 'r') as json_file:
        return json.load(json_file)
