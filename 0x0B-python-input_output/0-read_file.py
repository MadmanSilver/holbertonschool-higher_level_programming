#!/usr/bin/python3
""" Contains the read_file function. """


def read_file(filename=""):
    """ Reads and prints the content in a file. """
    with open(filename) as f:
        print(f.read(), end="")
