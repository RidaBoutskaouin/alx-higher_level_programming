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
