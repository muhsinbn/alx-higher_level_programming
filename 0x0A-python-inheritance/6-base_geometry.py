#!/usr/bin/python3
"""Module that creates a class"""


class BaseGeometry:
    """A class with public attribute area"""

    def area(self):
        """public instance method with exception when called"""
        raise Exception("area() is not implemented")
