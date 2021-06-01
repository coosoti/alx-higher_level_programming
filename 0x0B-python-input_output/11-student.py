#!/usr/bin/python3
"""class Student documentation"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """instantiaton function for the class Student

        Args:
            first_name (str): first name of a student
            last_name (str): last name of a student
            age (int): age of a student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance

        Args:
            attrs (python objects): objects to be returned

        """
        if not isinstance(attrs, list):
            return self.__dict__
        for attribute in attrs:
            if not isinstance(attribute, str):
                return self.__dict__
        new_dict = {}
        for str_att in attrs:
            if str_att in self.__dict__.keys():
                new_dict[str_att] = self.__dict__[str_att]
        return new_dict

    def reload_from_json(self, json):
        """this function replaces all attributes of the student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
