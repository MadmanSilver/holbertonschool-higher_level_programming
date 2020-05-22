#!/usr/bin/python3
""" Contains a function to print a square. """


def print_square(size):
    """ Prints a square to stdout as #s. """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for y in range(size):
        for x in range(size):
            print("#", end="")
        print("")
