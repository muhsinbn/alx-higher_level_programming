#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    """
    Finds all multiples of 2 in a list
    ...

    Parameters
    ----------
    my_list : list
        The list to check

    Return:
        A new list with True or False, depending
         on whether the integer at the same position
         in the original list is a multiple of 2
    """
    new = my_list.copy()

    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            new[i] = 1
        else:
            new[i] = 0
    return new
