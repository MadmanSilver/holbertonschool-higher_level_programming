#!/usr/bin/python3
""" Contains the to_json_string function. """
import json


def to_json_string(my_obj):
    """ Creates a JSON representation of an object. """
    return json.dumps(my_obj)
