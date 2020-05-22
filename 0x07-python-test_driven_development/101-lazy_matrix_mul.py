#!/usr/bin/python3
""" Contains lazy_matrix_mul function. """
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies two matrices. """
    return numpy.matmul(m_a, m_b)
