#!/usr/bin/python3
"""Module that creates a class"""


class BaseGeometry:
    """A class with public attribute area"""

    def area(self):
        """public instance method with exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance that validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
