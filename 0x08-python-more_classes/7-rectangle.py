#!/usr/bin/python3
"""This module writes a class Rectangle that defines a rectangle"""


class Rectangle:
    """Representation of a rectangle
    class variable to keep track of the number of instances
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter to the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance method that returns the area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """public instance method that returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """String representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (
                "\n".join(
                    [str(self.print_symbol) * self.__width] * self.__height
                    )
                )

    def __repr__(self):
        """String representation for recreation using eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints the message with the number when instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
