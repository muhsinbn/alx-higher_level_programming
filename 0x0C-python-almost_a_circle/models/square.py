#!/usr/bin/python3
"""Module that defines a class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """Fuction initialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Property getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter function for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Public method to assign attributes"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs and not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Overridden __str__ method for Square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """public method that returns dictionary representation"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
