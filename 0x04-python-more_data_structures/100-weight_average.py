#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    div = 0
    for e in my_list:
        total += (e[0] * e[1])
        div += e[1]
    return total / div
