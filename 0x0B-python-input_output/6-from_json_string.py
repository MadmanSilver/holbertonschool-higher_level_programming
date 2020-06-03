#!/usr/bin/python3
""" Contains the from_json_string function. """
import json


def from_json_string(my_str):
    """ Creates an object from a JSON string. """
    return json.loads(my_str)
