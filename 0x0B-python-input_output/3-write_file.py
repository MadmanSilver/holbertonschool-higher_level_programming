#!/usr/bin/python3
""" Contains the write_file function. """


def write_file(filename="", text=""):
    """ Writes a string to a file and returns number of characters written. """
    with open(filename, "w") as f:
        return f.write(text)
