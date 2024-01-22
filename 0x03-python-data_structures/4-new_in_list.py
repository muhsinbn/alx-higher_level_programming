#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    """
    Replaces an element in a copy of a list at a specific position
    ...

    Parameters
    ----------
    my_list : list
        The list of elements
    idx : integer
        The given position
    element : the new element

    Return:
        The copy of the list if idx is negative or
        if idx out of range (> len(my_list))
    """

    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
