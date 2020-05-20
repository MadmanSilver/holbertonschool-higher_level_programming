#!/usr/bin/python3
"""Contains the Square class."""


class Square:
    """A square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes attributes.

        Args:
            size (int): size of the square
            position (tuple): position of the square

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """int: size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square

        Returns:
            The result.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square to stdout"""
        if self.__size == 0:
            print("")
            return
        for py in range(self.__position[1]):
            print("")
        for y in range(self.__size):
            for px in range(self.__position[0]):
                print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        res = ""
        if self.__size == 0:
            return res
        for py in range(self.__position[1]):
            res += "\n"
        for y in range(self.__size):
            for px in range(self.__position[0]):
                res += " "
            for x in range(self.__size):
                res += "#"
            if (y + 1 != self.__size):
                res += "\n"
        return res
