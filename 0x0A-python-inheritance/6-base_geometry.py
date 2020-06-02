#!/usr/bin/python3
""" Contains the BaseGeometry class. """


class BaseGeometry():
    """ The base class for geometry. """
    def area(self):
        """ Calculates the area. """
        raise Exception("area() is not implemented")
