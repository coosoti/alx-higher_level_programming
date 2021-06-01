#!/usr/bin/python3
"""to_json_string function documentation"""


import json


def to_json_string(my_obj):
    """this functin returns the JSON representation of an object(string)

    Args:
        my_obj (class object): the object to convert to a JSON string

    Return:
        JSON representation of the object
    """
    return json.dumps(my_obj)
