#!/usr/bin/python3
"""This is a simple add 2 integers function documentation"""


def add_integer(a, b=98):
    """Adds 2 integers

    Args:
        a (int): first value passed
        b (int, optional): second value to be passed

    Returns:
        The sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
