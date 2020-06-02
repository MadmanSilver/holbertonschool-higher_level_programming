#!/usr/bin/python3
""" Contains the BaseGeometry class. """


class BaseGeometry():
    """ The base class for geometry. """
    def area(self):
        """ Calculates the area. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value. """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
