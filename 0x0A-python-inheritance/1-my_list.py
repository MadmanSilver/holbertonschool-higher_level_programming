#!/usr/bin/python3
""" Contains the class MyList. """


class MyList(list):
    """ My custom list class! """
    def print_sorted(self):
        """ Prints a sorted version of the list. """
        new = self.copy()
        new.sort()
        print(new)
