#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    div = 0
    for e in my_list:
        total += (e[0] * e[1])
        div += e[1]
    return total / div
