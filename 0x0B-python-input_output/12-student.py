#!/usr/bin/python3
""" Contains the Student class. """


class Student():
    """ I'm a student! """
    def __init__(self, first_name, last_name, age):
        """ Initializes attributes. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Creates a JSON representation of self. """
        if type(attrs) is list:
            for e in attrs:
                if type(e) is not str:
                    return self.__dict__
        else:
            return self.__dict__
        res = {}
        for attr in self.__dict__.keys():
            if attr in attrs:
                res[attr] = self.__dict__[attr]
        return res
