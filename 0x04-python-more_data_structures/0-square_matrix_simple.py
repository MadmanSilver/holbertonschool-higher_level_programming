#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for l in matrix:
        res.append(list(map(sqr, l)))
    return res

def sqr(n):
    return n ** 2
