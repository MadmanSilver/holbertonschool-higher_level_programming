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

    def area(self):
        """ Calculates the area of the rectangle. """
        return self.width * self.height

    def perimeter(self):
        """ Calculates the perimeter of the rectangle. """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """ Returns a string representation of the rectangle. """
        res = ""
        if self.width == 0:
            return res
        for y in range(self.height):
            res += "#" * self.width
            if y + 1 != self.height:
                res += "\n"
        return res

    def __repr__(self):
        """ Returns a string that can be used with eval to duplicate. """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Prints a message when rectangle is deleted. """
        print("Bye rectangle...")
