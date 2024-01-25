#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    """
    Prints a dictionary by ordered keys
    ...

    Parameters
    ----------
    a_dictionary : dictionary
        the given dictionary

    Return:
        Nothing
    """
    for key in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(key, a_dictionary[key]))
