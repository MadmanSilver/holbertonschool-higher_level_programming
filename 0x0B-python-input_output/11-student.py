#!/usr/bin/python3
""" Contains the Student class. """


class Student():
    """ I'm a student! """
    def __init__(self, first_name, last_name, age):
        """ Initializes attributes. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Creates a JSON representation of self. """
        return self.__dict__
