#!/usr/bin/python3
"""class_to_json function documentation"""


def class_to_json(obj):
    """returns a dictionary representation of a python object - list, bool,
     str, int, dictionary, for JSON serialization"""

    return obj.__dict__
