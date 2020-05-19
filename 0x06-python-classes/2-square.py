#!/usr/bin/python3
"""Contains the Square class."""


class Square:
    """No functionality."""
    def __init__(self, size=0):
        """Sets the size with type protection.

        Args:
            size (int): size of the square

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
