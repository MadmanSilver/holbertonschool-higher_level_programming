#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    res = next(iter(a_dictionary))
    tmp = a_dictionary[res]
    for key in a_dictionary.keys():
        if a_dictionary[key] > tmp:
            res = key
            tmp = a_dictionary[key]
    return res
