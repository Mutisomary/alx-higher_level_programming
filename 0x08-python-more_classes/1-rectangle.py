#!/usr/bin/python3

"""creates a Rectangle class that defines a rectangle"""


class Rectangle:
    """A class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """" initializes a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves an attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """retrieve an attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the heuight of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
