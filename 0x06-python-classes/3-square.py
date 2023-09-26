#!/usr/bin/python3
"""creates a Square class"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0):
        """
        init of a square class
        Args:
            size (int): size of Square
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")

        self.__size = size

    def area(self):
        """returns the area of a square"""
        return self.__size**2
