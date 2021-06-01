#!/usr/bin/python3
"""load_from_json_file function documentation"""


import json


def load_from_json_file(filename):
    """this function creates an object from a 'JSON file'

    Args:
       filename (JSON file): file where an object is created from

    Return:
        JSON object represented by string in the file
    """
    with open(filename, "r", encoding='utf-8') as myFile:
        return json.loads(myFile.read())
    #   return json.load(myFile)
