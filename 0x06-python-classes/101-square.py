#!/usr/bin/python3
""" Documentation for a square class"""


class Square:
    """Represent a square class of quadrilateral with four equal sides

    Attributes:
        __size (int): size of a side of the square
        --position (tuple): position of the object when printed in 2D space
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square

        Args:
            size (int): size of a side of a square
            position (tuple): position of the square in 2D space

        Returns:
            None

        Raises:
            ValueError: When the value passed is less than 0
            TypeError: When the value passed is not an integer
        """
        self.size = size
        self.position = position

    def area(self):
        """calculates the area of a square

        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """returns the current size of the object but if called
        with a value the setter function overwrites the current size
        with the size passed

        Returns:
            The size of the current object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """resets the size of the object with the value passed

        Args:
            value (int): the new size of the square object

        Raises:
            ValueError: When the value passed is less than 0
            TypeError: When the value passed is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints the square object

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for rows in range(self.__size):
            for spaces in range(self.__position[0]):
                print(" ", end="")
            for columns in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """Returns the current position of the square objects

        Returns:
            the current position/coordinates of the square object
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ resets the position of the square object

        Args:
            value (tuple): position defined by tuple of two integers

        Raises:
            ValueError: when the values passed are less than 0
            TypeError:when values passed are not integers or two integers

        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        """String representation of a Square instance

        Returns:
            Formatted string representation of the square
        """
        if self.size == 0:
            return ""
        _str = "\n" * self.position[1] + (" " * self.position[0] +
                                          "#" * self.size + "\n") * self.size
        return _str[:-1]
