#!/usr/bin/python3
""" Contains the inherits_from function. """


def inherits_from(obj, a_class):
    """ Checks if an object is a child of a class. """
    return issubclass(type(obj), a_class) and not type(obj) is a_class
