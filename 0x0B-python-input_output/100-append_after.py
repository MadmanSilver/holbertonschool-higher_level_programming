#!/usr/bin/python3
""" Contains the append_after function. """


def append_after(filename="", search_string="", new_string=""):
    """ Inserts line of text in file after lines containing new_string. """
    with open(filename, "r+") as f:
        contents = f.readlines()
        for line in range(len(contents)):
            if search_string in contents[line]:
                contents.insert(line + 1, new_string)
        f.seek(0)
        f.truncate()
        f.writelines(contents)
