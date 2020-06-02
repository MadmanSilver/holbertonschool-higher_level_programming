#!/usr/bin/python3
""" Contains the function add_attribute. """


def add_attribute(obj, name, value):
    """ Adds an attribute to an object if possible. """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
