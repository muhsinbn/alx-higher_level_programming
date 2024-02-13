#!/usr/bin/python3
"""This module prints a square with the character #."""


def print_square(size):
    """Function that prints a square
    Args:
        size - must be an integer
    raises:
        TypeError with exception message "size must be an integer"
        if less than 0 raise ValueError("size must be >= 0)
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
