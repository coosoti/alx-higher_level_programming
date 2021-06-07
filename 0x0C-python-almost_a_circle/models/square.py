#!/usr/bin/python3
"""Documentation for square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the Square instance

        Args:
            size (int): size of the square
            x (int): x coordinate
            y (int): y coordinate
            id (int): id of the object
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter for size attribute

        Return:
            size of the square instance
        """
        return self.width

    @size.setter
    def size(self, value):
        """setter for size attribute

        Args:
            value (int): size of the square attribute
        """
        self.width = value
        self.height = value

    def __str__(self):
        """overrides the __str__ builtin method

        Return:
            informal string representation of the square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the square instance

        Args:
            args (list): list of arguments
            kwargs (dict): dictionary with key/value pair arguments
        """

        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns dictionary representation of a Square"""
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["size"] = self.size
        new_dict["x"] = self.x
        new_dict["y"] = self.y
        return new_dict
