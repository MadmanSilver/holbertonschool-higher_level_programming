#!/usr/bin/python3
""" Finds a peak """


def find_peak(list_of_integers):
    """ calls recursive peak """
    if not len(list_of_integers):
        return None
    return list_of_integers[peak(list_of_integers, 0,
                                 len(list_of_integers) - 1,
                                 len(list_of_integers))]


def peak(ar, lo, hi, ln):
    """ finds peak """
    mid = int(lo + (hi - lo) / 2)
    if (mid == 0 or ar[mid - 1] <= ar[mid]) and\
       (mid == ln - 1 or ar[mid + 1] <= ar[mid]):
        return mid
    elif mid > 0 and ar[mid - 1] > ar[mid]:
        return peak(ar, lo, mid - 1, ln)
    else:
        return peak(ar, mid + 1, hi, ln)
