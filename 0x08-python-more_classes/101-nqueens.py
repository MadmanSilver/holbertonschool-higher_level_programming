#!/usr/bin/python3
""" Program that calculates the N queens problem. """


import sys

argv = sys.argv
argc = len(argv)

if argc != 2:
    print("Usage: nqueens N")
    sys.exit(1)
if not argv[1].isnumeric():
    print("N must be a number")
    sys.exit(1)
N = int(argv[1])
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queens = []


def attackable(place):
    """ Checks if the place is prone to attack. """
    for q in queens:
        if place[0] == q[0] or place[1] == q[1]:
            return True
        if abs(place[0] - q[0]) == abs(place[1] - q[1]):
            return True
    return False


def inqueens(place):
    """ Checks if the spot is already taken. """
    for q in queens:
        if place[0] == q[0] and place[1] == q[1]:
            return True
    return False


def builder(place):
    """ Main brains. Checks every spot. """
    while place[0] < N:
        while place[1] < N:
            if not inqueens(place) and not attackable(place):
                queens.append(place.copy())
                if len(queens) == N:
                    print(queens)
                    queens.pop()
                    return
                builder(place.copy())
                queens.pop()
            place[1] += 1
        place[1] = 0
        place[0] += 1

builder([0, 0])
