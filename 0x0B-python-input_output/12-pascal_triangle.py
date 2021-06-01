#!/usr/bin/python3
"""pascal_triangle function documentation"""


def pascal_triangle(n):
    """this functions returns a list of lists of integers representing \
    a pascal triangle

    Args:
        n (int): number of rows of the pascal triangle

    Return:
        pascal triangle - a list of lists
    """

    if n <= 0:
        return ""

    p_triangle = [[1]]
    for cur_row in range(1, n):
        row = [1]
        r_prev = p_triangle[cur_row - 1]
        for el in range(1, cur_row):
            row.append(r_prev[el] + r_prev[el - 1])
        row.append(1)
        p_triangle.append(row)
    return p_triangle
