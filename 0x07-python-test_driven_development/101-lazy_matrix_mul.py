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
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if type(m_a[0]) is not list:
        raise TypeError("m_a must be a list of lists")
    if type(m_b[0]) is not list:
        raise TypeError("m_b must be a list of lists")
    if (m_a is None or m_a[0] is None):
        raise ValueError("m_a can't be empty")
    if (m_b is None or m_b[0] is None):
        raise ValueError("m_b can't be empty")
    # check that all data in matrix m_a are numbers (int/float)
    for i in range(0, len(m_a)):
        for j in range(0, len(m_a[0])):
            if (type(m_a[i][j]) not in [int, float]):
                raise TypeError("m_a should contain only integers or floats")
    # check that all data in matrix m_a are numbers (int/float)
    for i in range(0, len(m_b)):
        for j in range(0, len(m_b[0])):
            if (type(m_b[i][j]) not in [int, float]):
                raise TypeError("m_b should contain only integers or floats")
    # check rows len m_b
    base_lenght = len(m_a[0])
    for i in range(0, len(m_a)):
        if len(m_a[i]) != base_lenght:
            raise TypeError("each row of m_a must be of the same size")

    # check rows len m_b
    base_lenght = len(m_b[0])
    for i in range(0, len(m_b)):
        if len(m_b[i]) != base_lenght:
            raise TypeError("each row of m_b must be of the same size")

    # check number of columns in A is different than number of rows in B
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")
    numpy_ma = np.array(m_a)
    numpy_mb = np.array(m_b)
    result = numpy_ma.dot(numpy_mb)
    return result
