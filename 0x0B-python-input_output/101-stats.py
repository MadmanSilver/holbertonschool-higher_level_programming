#!/usr/bin/python3
""" Calculates some metrics. """
import sys

lc = 0
size = 0
codes = {"200": 0, "301": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
for line in sys.stdin:
    lc += 1
    split = line.split()
    size += int(split[-1])
    if split[-2] in codes.keys():
        codes[split[-2]] += 1
    if lc % 10 == 0:
        print("File size: {}".format(size))
        for code in codes.keys():
            if codes[code] != 0:
                print("{}: {}".format(code, codes[code]))
