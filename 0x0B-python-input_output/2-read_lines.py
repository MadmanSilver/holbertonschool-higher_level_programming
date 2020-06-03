#!/usr/bin/python3
""" Contains the read_lines function. """


def read_lines(filename="", nb_lines=0):
    """ Reads n lines from a text file. """
    i = 0
    with open(filename) as f:
        for l in f:
            i += 1
            print(l, end="")
            if i == nb_lines:
                break
