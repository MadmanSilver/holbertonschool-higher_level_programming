#!/usr/bin/python3
""" Contains the Rectangle class. """


class Rectangle:
    """ Defines a rectangle. """
    def __init__(self, width=0, height=0):
        """ Sets up the rectangle instance. """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Height of the rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
