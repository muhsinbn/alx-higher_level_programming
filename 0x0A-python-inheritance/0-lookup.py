#!/usr/bin/python3
"""Module returns the list of available attributes and methods of an object"""


def lookup(obj):
    """The function that returns the list"""
    return dir(obj)
