#!/usr/bin/python3
"""Module that contains a class BaseGeometry"""


class BaseGeometry:
    """Empty class BaseGeometry"""

    def area(self):
        """Method that raises an Exception with the message area()
        is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Method that initializes an instance of class Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
