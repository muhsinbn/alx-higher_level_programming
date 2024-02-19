#!/usr/bin/python3
"""Module that checks if object is exactly an instance of the specified
class and returns True, or return False if otherwise
"""


def is_same_class(obj, a_class):
    """Initialization of the function"""
    if type(obj) == a_class:
        return True
    return False
