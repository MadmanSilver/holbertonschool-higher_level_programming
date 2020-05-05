#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for y in matrix:
        for x in range(0, len(y)):
            if x == len(y) - 1:
                print("{:d}".format(y[x]))
            else:
                print("{:d}".format(y[x]), end=' ')
    if len(matrix[0]) < 1:
        print("")
