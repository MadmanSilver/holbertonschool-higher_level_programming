#!/usr/bin/python3
""" Contains a function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for e in matrix:
        if type(e) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        l = len(matrix[0])
        if len(e) != l:
            raise TypeError("Each row of the matrix must have the same size")
        for i in e:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda y: list(map(lambda
                                       x: round(x / div, 2), y)), matrix))
