#!/usr/bin/python3
"""Module returns True if object is an instance of, or if the object
is an instance of a class that inherited from the specified class
otherwise False
"""


def is_kind_of_class(obj, a_class):
    """initialization of the function"""
    if isinstance(obj, a_class):
        return True
    return False
