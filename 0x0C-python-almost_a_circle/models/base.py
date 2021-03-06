#!/usr/bin/python3
""" Contains the Base class. """
import json


class Base():
    """ I'm the base for everything! """
    __nd_objects = 0

    def __init__(self, id=None):
        """ Initializes the attributes. """
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries. """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_bjs to a file. """
        if list_objs and len(list_objs) > 0:
            objs = list_objs.copy()
            for i in range(len(objs)):
                objs[i] = objs[i].to_dictionary()
        else:
            objs = []
        with open("{}.json".format(cls.__name__), 'w') as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation. """
        if not json_string or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set. """
        if cls.__name__ == "Square":
            new = cls(1)
        else:
            new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances. """
        try:
            with open("{}.json".format(cls.__name__), 'r') as f:
                l = cls.from_json_string(f.read())
                for i in range(len(l)):
                    l[i] = cls.create(**l[i])
        except:
            return []
        return l
