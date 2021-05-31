#!/usr/bin/python3
"""inherited class checker documentation"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instance of or an instance of class that inherited \
       from a specified class

    Return:
        True is the obj is an instance, False otherwise.
    """

    return (isinstance(obj, a_class))
