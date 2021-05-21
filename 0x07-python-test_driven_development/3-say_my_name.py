#!/usr/bin/python3
"""say_my_name function documentation"""


def say_my_name(first_name, last_name=""):
    """this function will print My name is <first name> <last name> passed to it

    Args:
        first_name (str): the first name
        last_name (str, optional): the last name

    Raises:
        TypeError: if the first_name or last_name passed are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
