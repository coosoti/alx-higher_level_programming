#!/usr/bin/python3
"""Matrix Division Documentation"""


def matrix_divided(matrix, div):
    """function that divides a matrix by an int or a float

    Args:
        matrix (list): matrix to be divided
        div (int, float): the number to divide the matrix by

    Returns:
        new matrix with each element resultant of the division
    """

    if matrix is None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    for i in matrix:
        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    size = None
    for l in matrix:
        if size is None:
            size = len(l)
        if size != len(l):
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not isinstance(matrix[i][j], (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        new_matrix = []
        for i in matrix:
            new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
        return new_matrix
