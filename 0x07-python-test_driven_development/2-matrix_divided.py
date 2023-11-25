#!/usr/bin/python3
"""A module that divide matrix"""


def matrix_divided(matrix, div):
    """
    Function that divide matrix by div
    Args:
        matrix = first list of lists
        b = second divided int not zero
    Raises:
        TypeError: if matrix not lists of lists of integers or floats
        TypeError: if row of the matrix not be of the same size
        TypeError: if div not a number
        ZeroDivisionError: while division by zero
    Returns:
        divided matrix with div
    """
    a = 0
    h = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    while a < len(matrix):
        if not isinstance(matrix, list):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        b = 0
        g = []
        while b < len(matrix[a]):
            if not isinstance(matrix[a], list):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            if not isinstance(matrix[a][b], (int, float)):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            g.append(round(matrix[a][b] / div, 2))
            b += 1
        if len(matrix[a]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        h.append(g)
        a += 1
    return h
