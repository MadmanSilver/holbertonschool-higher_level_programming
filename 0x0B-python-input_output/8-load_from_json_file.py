#!/usr/bin/python3
""" Contains the load_from_json_file function. """
import json


def load_from_json_file(filename):
    """ Converts and saves an object into a JSON file. """
    with open(filename, "r") as f:
        return json.load(f)
