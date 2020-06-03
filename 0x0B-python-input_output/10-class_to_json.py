#!/usr/bin/python3
""" Contains the class_to_json function. """


def class_to_json(obj):
    """ Returns the JSON representation of all attributes of a class. """
    return obj.__dict__
