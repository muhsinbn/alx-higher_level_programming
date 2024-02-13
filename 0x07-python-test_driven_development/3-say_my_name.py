#!/usr/bin/python3
"""This function prints a name"""


def say_my_name(first_name, last_name=""):
    """
    The module prints out names
    Args:
        first_name
        lastname
    Raises:
        TypeError if first_name and last_name are not string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
