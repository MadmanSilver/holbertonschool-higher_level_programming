#!/usr/bin/python3
i = 25
while i > -1:
    if i % 2:
        m = 97
    else:
        m = 65
    print("{}".format(chr(i + m)), end="")
    i -= 1
