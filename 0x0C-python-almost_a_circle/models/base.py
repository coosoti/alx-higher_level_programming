#!/usr/bin/python3
"""Documentation for Base class"""


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
