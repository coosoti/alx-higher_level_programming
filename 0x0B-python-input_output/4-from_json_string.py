#!/usr/bin/python3
"""from_json_string function documentation"""


import json


def from_json_string(my_str):
    """this function returns an object(python data structure) represent a JSON \
    string

    Args:
        my_str (JSON string): json string to convert to an python object

    Return:
        object - python data structure
    """
    return json.loads(my_str)
