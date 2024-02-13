#!/usr/bin/python3
"""This module divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): The input matrix as a list of lists.
        div (int or float): The divisor.

    Returns:
        list: A new matrix where each element is the result of division
        rounded to 2 decimal place.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats
        If each row of the matix does not have the same size
        if div is not a number (integer or float).

        ZeroDivisionError: If div is equal to 0

    """
    if not all(
            isinstance(row, list) and
            all(isinstance(num, (int, float)) for num in row)
            for row in matrix
            ):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(num / div, 2) for num in row] for row in matrix]
    return result
