#!/usr/bin/python3

"""subclass of Base"""

from models.base import Base


class Rectangle(Base):
    """defining a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve the attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """retrieve the e=x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the value if x"""
        if type(value) is not int:
            raise TypeError("x must be an int")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieve the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an int")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get the area"""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle with # characters"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """string representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """"assigns an argument to each attribute"""

        up = ["id", "width", "height", "x", "y"]
        if (args):
            for i in range(len(args)):
                setattr(self, up[i], args[i])

        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """return the dictionary representation of rectangle"""
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
