#!/usr/bin/python3
""" Contains the Rectangle class. """


class Rectangle:
    """ Defines a rectangle. """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Sets up the rectangle instance. """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            res += "{}".format(self.print_symbol) * self.width
            if y + 1 != self.height:
                res += "\n"
        return res

    def __repr__(self):
        """ Returns a string that can be used with eval to duplicate. """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Prints a message when rectangle is deleted. """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area. """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Constructor for a square using the Rectangle class. """
        return Rectangle(size, size)
