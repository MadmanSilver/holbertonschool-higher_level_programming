#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)
        if ord(i) > 96 and ord(i) < 123:
            num -= 32
        print("{}".format(chr(num)), end="")
    print("")
