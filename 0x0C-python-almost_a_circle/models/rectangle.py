#!/usr/bin/python3
"""Documentation for Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of Rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coordinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): id of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width attribute

        Args:
            value (int): value to set to width to
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter of height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height attribute

        Args:
            value (int): the value to set the height to
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the x coordinate attribute

        Args:
            value (int): the value to set the x attribute to
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter of y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of the y coordinate attribute

        Args:
            value (int): the value to set the y attribute to
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle instance

        Return:
            the area of the current rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """Displays/prints the Rectangle instance with a character #
        sign
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """Overrides the __str__ method to print specified informal string
        representation of the Rectangle instance
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates the attributes in a list *args or **kwargs

        Args:
            *args (list): non-keyworded argument list
            **kwargs (dict): keyworded argument list
        """
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns a dictionary representation of a Rectangle instance"""
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["width"] = self.width
        new_dict["height"] = self.height
        new_dict["x"] = self.x
        new_dict["y"] = self.y
        return new_dict
