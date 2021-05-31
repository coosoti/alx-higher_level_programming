#!/usr/bin/python3
"""class inheritance checker"""


def inherits_from(obj, a_class):
    """checks if an obj is a subclass of a_class

    Return:
        True if an obj is a subclass of a_class, False otherwise
    """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
