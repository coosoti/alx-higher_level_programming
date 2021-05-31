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

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
