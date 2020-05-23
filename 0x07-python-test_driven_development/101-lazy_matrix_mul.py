#!/usr/bin/python3
"""
This file multiplies two matrix
Written by: daorejuela1
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function automatically ident text.

    Args:
        ma_a: first matrix.
        ma_b: second matrix.

    Returns:
        matrix with mult value.

    Raises:
        TypeError: if matrices are empty
        doesnt have int/float or
        cant multiply.
    """
    if type(m_a) is not list:
        raise TypeError("m_a is not a list")
    if type(m_b) is not list:
        raise TypeError("m_b is not a list")
    try:
        if type(m_a[0]) is not list:
            raise TypeError("m_a is not a list of lists")
    except IndexError:
        raise ValueError("m_a is empty")
    try:
        if type(m_b[0]) is not list:
            raise TypeError("m_b is not a list of lists")
    except IndexError:
        raise ValueError("m_b is empty")
    if (len(m_a[0]) == 0):
        raise ValueError("m_a is empty")
    if (len(m_b[0]) == 0):
        raise ValueError("m_b is empty")
    # check that all data in matrix m_a are numbers (int/float)
    for i in range(0, len(m_a)):
        for j in range(0, len(m_a[i])):
            if (type(m_a[i][j]) not in [int, float]):
                raise ValueError("m_a contains a not number")
    # check that all data in matrix m_a are numbers (int/float)
    for i in range(0, len(m_b)):
        for j in range(0, len(m_b[i])):
            if (type(m_b[i][j]) not in [int, float]):
                raise ValueError("m_b contains a not number")
    # check rows len m_b
    base_lenght = len(m_a[0])
    for i in range(0, len(m_a)):
        if len(m_a[i]) != base_lenght:
            raise TypeError("m_a rows are not even")

    # check rows len m_b
    base_lenght = len(m_b[0])
    for i in range(0, len(m_b)):
        if len(m_b[i]) != base_lenght:
            raise TypeError("m_b rows are not even")

    # check number of columns in A is different than number of rows in B
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a colums are not m_b rows")
    numpy_ma = np.array(m_a)
    numpy_mb = np.array(m_b)
    result = numpy_ma.dot(numpy_mb)
    return result
