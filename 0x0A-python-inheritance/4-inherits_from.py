#!/usr/bin/python3
"""Module Checks if an object is an inherited instance of a class
Args:
    obj (any): the object to check
    a_class (type): The class to match the type of the obj to

Returns:
    if obj is an inherited instance of a_class - True
    Otherwise - False
"""


def inherits_from(obj, a_class):
    """initialization of the function"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
