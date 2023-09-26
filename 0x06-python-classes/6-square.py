#!/usr/bin/python3
"""creates a Square class"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        init of a square class
        Args:
            size (int): size of Square
        """
        self.__size = size
        self.__position = position

    def area(self):
        """returns the area of a square"""
        return self.__size**2

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)

        for j in range(self.__position[1]):
            print()
        for k in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
            print()

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if isinstance(value, tuple) is not True or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[0], int) is not True or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[1], int) is not True or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
