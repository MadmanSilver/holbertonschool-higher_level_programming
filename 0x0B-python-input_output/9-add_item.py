#!/usr/bin/python3
""" Loads, adds, and saves arguments to a Python list stored in JSON. """
import json
import sys
load = __import__('8-load_from_json_file').load_from_json_file
save = __import__('7-save_to_json_file').save_to_json_file
args = sys.argv[1:]
with open("add_item.json", "a") as f:
    try:
        l = load("add_item.json")
    except:
        l = []
    for e in args:
        l.append(e)
    save(l, "add_item.json")
