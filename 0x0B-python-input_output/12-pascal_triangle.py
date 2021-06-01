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
    p_triangle = []
    r_prev = [1]
    row = 0

    if n <= 0:
        return []
    while row < n - 1:
        cur_row = []
        cur_row.append(r_prev[0])
        i = 0
        while i < row:
            cur_row.append(r_prev[i] + r_prev[i + 1])
            i += 1
        cur_row.append(r_prev[len(r_prev) - 1])
        p_triangle.append(cur_row)
        r_prev = cur_row
        row += 1
    return p_triangle
