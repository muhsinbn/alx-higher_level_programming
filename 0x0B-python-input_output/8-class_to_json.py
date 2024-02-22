#!/usr/bin/python3
"""Module that returns dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization
of an object.
"""


def class_to_json(obj):
    """Initialization of the function"""
    return obj.__dict__
