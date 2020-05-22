#!/usr/bin/python3
""" Contains the matrix_mul function. """


def matrix_mul(m_a, m_b):
    """ Multiplies matrices. """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for l in m_a:
        if type(l) is not list:
            raise TypeError("m_a must be a list of lists")
    for l in m_b:
        if type(l) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for l in m_a:
        for i in l:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for l in m_b:
        for i in l:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    ln = len(m_a[0])
    for l in m_a:
        if len(l) != ln:
            raise ValueError("each row of m_a must be of the same size")
    ln = len(m_b[0])
    for l in m_b:
        if len(l) != ln:
            raise ValueError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = []
    tmp = 0
    y_a = 0
    x_a = 0
    y_b = 0
    x_b = 0
    while y_a < len(m_a):
        res.append([])
        while x_b < len(m_b[0]):
            while x_a < len(m_a[0]) or y_b < len(m_b):
                if x_a >= len(m_a[0]):
                    tmp += m_b[y_b][x_b]
                elif y_b >= len(m_b):
                    tmp += m_a[y_a][x_a]
                else:
                    tmp += m_a[y_a][x_a] * m_b[y_b][x_b]
                x_a += 1
                y_b += 1
            res[y_a].append(tmp)
            tmp = 0
            x_a = 0
            y_b = 0
            x_b += 1
        x_b = 0
        y_a += 1

    return res
