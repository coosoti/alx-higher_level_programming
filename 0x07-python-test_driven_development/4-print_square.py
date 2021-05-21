#!/usr/bin/python3
"""print_square function documentation"""


def print_square(size):
    """function that prints a square of length size using character '#'

    Args:
        size (int): the length of the side of the square

    Raises:
        TypeError: size must be an integer
        ValueError: the size of the length is negative
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
