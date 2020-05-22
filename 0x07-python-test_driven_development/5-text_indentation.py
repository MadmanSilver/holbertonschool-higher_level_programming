#!/usr/bin/python3
""" Contains the text_indentation function. """


def text_indentation(text):
    """ Prints a text with 2 new lines after specific characters. """
    if type(text) is not str:
        raise TypeError("text must be a string")

    new = ""
    i = 0

    while i < len(text):
        new += text[i]
        if text[i] in ".?:":
            while i + 1 != len(text) and text[i + 1] in " ":
                i += 1
            new += "\n\n"
        i += 1

    print(new, end="")
