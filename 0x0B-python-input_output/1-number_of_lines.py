#!/usr/bin/python3
""" Contains the number_of_lines function. """


def number_of_lines(filename=""):
    """ Returns the number of lines in a file. """
    with open(filename) as f:
        return len(list(f))
