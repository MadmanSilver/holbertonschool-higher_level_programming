#!/usr/bin/python3
""" Contains the Rectangle class. """
from models.base import Base


class Rectangle(Base):
    """ I'm a rectangle! """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes all attributes. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height of the rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def y(self):
        """ Y position of the rectangle. """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """ X position of the rectangle. """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """ Calculates the area of the rectangle. """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle to stdout as #s. """
        print("\n" * self.__y, end="")
        for row in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ Returns a string representation of the rectangle. """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,\
            self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Updates the values of width, height, x, and y. """
        l = len(args)
        if l > 0:
            self.id = args[0]
        if l > 1:
            self.width = args[1]
        if l > 2:
            self.height = args[2]
        if l > 3:
            self.x = args[3]
        if l > 4:
            self.y = args[4]

        if not l > 0:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "width" in kwargs.keys():
                self.width = kwargs["width"]
            if "height" in kwargs.keys():
                self.height = kwargs["height"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns a dictionary representation of the rectangle. """
        return {'id': self.id, 'width': self.__width,\
            'height': self.__height, 'x': self.__x, 'y': self.__y}
