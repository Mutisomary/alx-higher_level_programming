#!/usr/bin/python3

"""8-rectangle.py module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defining a subclass BaseGeometry"""

    def __init__(self, width, height):
        """"initializing a rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
