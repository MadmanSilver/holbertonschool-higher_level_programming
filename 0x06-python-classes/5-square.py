#!/usr/bin/python3
"""Contains the Square class."""


class Square:
    """A square."""
    def __init__(self, size=0):
        """Initializes attributes.

        Args:
            size (int): size of the square

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """int: size of the sqaure"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets with type protection."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            The result.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square to stdout represented as #"""
        if self.__size == 0:
            print("")
        for y in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print("")
