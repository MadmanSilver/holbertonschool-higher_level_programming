#!/usr/bin/python3
"""Contains the Square class."""


class Square:
    """Just a square."""
    def __init__(self, size=0):
        """Sets size with type protection

        Args:
            size (int): size of the square

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            The result.
        """
        return self.__size ** 2
