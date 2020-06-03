#!/usr/bin/python3
""" Contains the save_to_json_file function. """
import json


def save_to_json_file(my_obj, filename):
    """ Converts and saves an object into a JSON file. """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
