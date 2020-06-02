#!/usr/bin/python3
""" Contains the lookup function. """


def lookup(object):
    """ Returns a list of all attributes and methods of an object. """
    return list(dir(object))
