#!/usr/bin/python3
"""Module that creates a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """instantiation of class with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """public instance that searches for the area"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
