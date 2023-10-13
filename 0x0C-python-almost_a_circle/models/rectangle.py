#!/usr/bin/python3
"""This module provides a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """This class defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This method initializes a rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This method returns the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """This method sets the width of a rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """This method returns the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """This method sets the height of a rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >=0")
        self.__height = value

    @property
    def x(self):
        """This method returns the x of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """This method sets the x of a rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >=0")
        self.__x = value

    @property
    def y(self):
        """This method returns the y of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """This method sets the y of a rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >=0")
        self.__y = value

    def area(self):
        """This method returns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """This method prints a rectangle"""
        if self.__width == 0 or self.__height == 0:
            print()
            return

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """This method returns a string representation of a rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """This method updates a rectangle"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
