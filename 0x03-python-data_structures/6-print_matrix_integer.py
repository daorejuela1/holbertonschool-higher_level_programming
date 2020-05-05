#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	"""Prints a matrix in python"""
	for col in range(0, 3):
		for row in range(0, 3):
			print("{:d}".format(matrix[col][row]), end=", ")
			if (row == 2):
				print()
