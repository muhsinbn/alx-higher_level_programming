#!/usr/bin/python3
"""Defines a function that writes an object to a text file using JSON rep"""


import json


def save_to_json_file(my_obj, filename):
    """initialization of the function"""
    with open(filename, 'w') as json_file:
        return json.dump(my_obj, json_file)
