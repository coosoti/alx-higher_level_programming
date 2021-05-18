#!/usr/bin/python3
""" Documentation for a square class"""


class Square:
    """Represent a square class of quadrilateral with four equal sides

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes a new square

        Args:
            size (int): size of a side of a square

        Returns: None
        """
        self.__size = size
