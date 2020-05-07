#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(i ** 2 for i in x[0:len(x)]), matrix)))
