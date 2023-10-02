#!/usr/bin/python3


""" Module that creates a Rectangle class """


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """gets area"""
        return self.__width * self.__height

    def perimeter(self):
        """gets perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """prints rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (self.__height * ("#" * self.__width + "\n"))[:-1]

    def __repr__(self):
        """string representation of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """deletes rectangle"""
        print("Bye rectangle...")
