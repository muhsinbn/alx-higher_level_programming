#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    """
    Prints all integers of a list, in reverse order
    ...

    Parameters
    ----------
    my_list : list
        The list of elements
    """
    if my_list:
        for count in reversed(my_list):
            print("{:d}".format(count))
