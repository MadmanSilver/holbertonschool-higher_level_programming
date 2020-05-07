#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    res = 0
    conv = []
    dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for e in list(roman_string):
        if e in dic:
            conv.append(dic[e])
    conv.append(0)
    for i in range(len(conv) - 1):
        if conv[i] < conv[i + 1]:
            res -= conv[i]
        else:
            res += conv[i]
    return res
