#!/usr/bin/python3
"""Module square that inherits from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class defination"""
    def __init__(self, size):
        """Instantiation of the class square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """string representation of square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
