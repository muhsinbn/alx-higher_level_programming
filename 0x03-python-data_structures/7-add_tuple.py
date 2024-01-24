#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    """
    Adds 2 tuples
    ...

    Parameters
    ----------
    tuple_a : tuple
        The first tuple
    tuple_b : tuple
        The second tuple

    Return:
        A tuple with 2 integers
    """
    lenA = len(tuple_a)
    lenB = len(tuple_b)
# check for tuple_a
    if lenA < 1:
        tuple_a = (0, 0)
    elif lenA < 2:
        tuple_a = (tuple_a[0], 0)

# check for tuple_b
    if lenB < 1:
        tuple_b = (0, 0)
    elif lenB < 2:
        tuple_b = (tuple_b[0], 0)

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
