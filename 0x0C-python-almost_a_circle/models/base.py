#!/usr/bin/python3
"""Documentation for Base class"""


import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation function for Base instance

        Args:
            id (int): the id of the instance
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances which inherits from Base
        """
        filename = cls.__name__ + ".json"
        list_objects = []
        if list_objs is not None:
            for i in list_objs:
                list_objects.append(cls.to_dictionary(i))
        with open(filename, 'w', encoding='utf-8') as myFile:
            myFile.write(cls.to_json_string(list_objects))
