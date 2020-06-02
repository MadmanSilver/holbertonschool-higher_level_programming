#!/usr/bin/python3
""" Contains the MyInt class. """


class MyInt(int):
    """ I'm a rebel! """
    def __eq__(self, other):
        """ Sike! """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Hehe... gotcha! """
        return super().__eq__(other)
