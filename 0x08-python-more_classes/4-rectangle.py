#!/usr/bin/python3
"""rectangle class documentation"""


class Rectangle:
    """Initializes a rectangle class"""

    def __init__(self, width=0, height=0):
        """instantiation of a rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Returns the width of the instance"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle instance

        Args:
            value (int): the width of the rectangle instance

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the width of the instance"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle instance

        Args:
            value (int): the height of the rectangle instance

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle instance"""

        return self.__height * self.__width

    def perimeter(self):
        """returns the the perimeter of a rectangle instance"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns the printable string representation of the rectangle"""
        str_rep = ""
        if self.__width != 0 and self.__height != 0:
            str_rep += "\n".join("#" * self.__width
                                 for j in range(self.__height))
        return str_rep

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
