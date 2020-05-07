#!/usr/bin/python3
def uniq_add(my_list=[]):
    tmp = []
    res = 0
    for i in my_list:
        if i not in tmp:
            res += i
            tmp.append(i)
    return res
