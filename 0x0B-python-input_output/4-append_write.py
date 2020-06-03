#!/usr/bin/python3
""" Contains the append_write function. """


def append_write(filename="", text=""):
    """ Appends a string to a file and returns number of characters. """
    with open(filename, "a") as f:
        return f.write(text)
