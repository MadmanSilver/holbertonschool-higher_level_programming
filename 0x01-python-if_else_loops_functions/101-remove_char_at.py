#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    i = 0
    while i < len(str):
        if i != n:
            new += str[i]
        i += 1
    return new
