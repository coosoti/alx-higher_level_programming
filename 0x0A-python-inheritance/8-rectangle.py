#!/usr/bin/python3
"""BaseGeometry class Documentation"""


class BaseGeometry:
    """creates BaseGeometry class"""

    def area(self):
        """area function for an instance of class BaseGeomtry"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate an integer value

        Args:
            name (str): the name(string)
            value (int): the int value to be validated

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less or equal to 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """a Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """instantiation of the rectangle instance

        Args:
            width (int) : the width of the rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
