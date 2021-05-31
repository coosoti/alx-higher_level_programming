#!/usr/bin/python3
"""BaseGeometry class Documentation"""


class BaseGeometry:
    """class with public instance methods"""

    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if type(value) is not int:
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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
