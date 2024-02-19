#!/usr/bin/python3
"""Class that inherits from list"""


class MyList(list):
    """the class that inherits from list"""
    def __init__(self):
        """Initiates the object"""
        super().__init__()

    def print_sorted(self):
        """public instance method that prints sorted list"""
        new = sorted(self)
        print(new)
