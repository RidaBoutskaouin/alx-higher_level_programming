#!/usr/bin/python3
"""This module provides a Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """This method initializes a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This method prints the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """This method returns the size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """This method sets the size of a square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This method updates the square"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
