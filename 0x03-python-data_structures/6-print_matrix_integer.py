#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    """
    Prints a matrix of integers
    ...

    Parameters
    ----------
    matrix : list (of lists)
        The list to print

    Return:
        None
    """
    for i in matrix:
        print(" ".join("{:d}".format(j) for j in i))
