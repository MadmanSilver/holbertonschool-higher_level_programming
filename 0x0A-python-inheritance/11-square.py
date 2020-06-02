#!/usr/bin/python3
""" Contains the class Square. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ It's a sqaure. """
    def __init__(self, size):
        """ Initializes the sqaure. """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Returns a string description of the sqaure. """
        return "[Square] {}/{}".format(self.__size, self.__size)
