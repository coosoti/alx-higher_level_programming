#!/usr/bin/python3
""" Documentation for a square class"""


class Square:
    """Represent a square class of quadrilateral with four equal sides

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes a new square

        Args:
            size (int): size of a side of a square

        Returns:
            None

        Raises:
            ValueError: When the value passed is less than 0
            TypeError: When the value passed is not an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates the area of a square

        Returns:
            The area of the square
        """
        return (self.__size) ** 2
