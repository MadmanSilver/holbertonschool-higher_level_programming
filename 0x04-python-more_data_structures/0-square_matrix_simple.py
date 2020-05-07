#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for l in matrix:
        res.append(list(map(lambda x: x ** 2, l)))
    return res
