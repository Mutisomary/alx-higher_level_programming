#!/usr/bin/python3


class Rectangle:
    """"A class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve the width attribute"""
        return self.__width

    def width(self, value):
        """sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width

    @property
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height

    def area(self):
        """calculate the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if width == 0 or height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str___(self):
        """sets the print behaviour of the string"""
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += '#' * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        """Return a string representation"""
        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return 'Rectangle(' + w + ', ' + h + ')'
