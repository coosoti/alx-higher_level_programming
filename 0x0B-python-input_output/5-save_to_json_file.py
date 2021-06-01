#!/usr/bin/python3
"""save_to_json function documentation"""


import json


def save_to_json_file(my_obj, filename):
    """this function writes an object to a text file, using JSON \
    representation

    Args:
        my_obj (class object): the object to convert to JSON string
        filename (file): the file to write to
    """
    with open(filename, "w", encoding='utf-8') as myFile:
        obj_json = json.dumps(my_obj)
        myFile.write(obj_json)
