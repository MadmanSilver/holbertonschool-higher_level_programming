#!/usr/bin/python3
""" Contains the is_same_class function. """


def is_same_class(obj, a_class):
    """ Checks if an object is and instance of an exact class. """
    return type(obj) is a_class
