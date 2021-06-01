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

    def to_json(self):
        """returns a dictionary representation of a Student instance"""
        return self.__dict__
