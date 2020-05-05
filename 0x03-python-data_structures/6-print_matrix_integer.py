#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix in python"""
    if matrix[0]:
        num_lists = len(matrix)
        len_list = len(matrix[0])
        for col in range(0, num_lists):
            for row in range(0, len_list):
                print("{:d}".format(matrix[col][row]), end="")
                if (row == len_list - 1):
                    print()
                else:
                    print("", end=", ")
    else:
        print()
