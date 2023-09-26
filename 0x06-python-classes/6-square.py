#!/usr/bin/python3


class Square:
    """Square class with private attribute size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize data"""
        self.__size = size
        self.__position = position

    def area(self):
        """Return area of square"""
        return self.__size**2

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be positive")
        self.__size = value

    @property
    def position(self):
        """Getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method"""
        if (
            len(value) != 2
            or isinstance(value[0], int) is not True
            or isinstance(value[1], int) is not True
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
