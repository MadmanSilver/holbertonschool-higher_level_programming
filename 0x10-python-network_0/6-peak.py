#!/usr/bin/python3
""" Finds a peak """


def find_peak(list_of_integers):
    """ finds a peak """
    num = list_of_integers
    res = None
    for i in range(len(num)):
        res = num[i]
        if num[i - 1] < num[i] and num[i + 1] < num[i]:
            return num[i]
        if num[i] != num[i - 1]:
            res = None
    return res
