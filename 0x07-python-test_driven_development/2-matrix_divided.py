#!/usr/bin/python3
"""

matrix_divide a new matrix divided by div

"""
def matrix_divided(matrix, div):
	"""this functions divides a matrix by the num div"""
	if matrix is None:
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	if type(matrix) is not list or type(matrix[0]) is not list:
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	#Check for all data in the matrix
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[0])):
			if (type(matrix[i][j]) is not int and type(matrix[i][j]) is not float):
				raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	#Check for row sizes
	normal_size = len(matrix[0])
	for i in range(0, len(matrix)):
		if (normal_size != len(matrix[i])):
			raise TypeError("Each row of the matrix must have the same size")
	#Check for datatype of div
	if (type(div) is not int and type(div) is not float):
		raise TypeError("div must be a number")
	#Divison by zero case
	if (div == 0):
		raise ZeroDivisionError("division by zero")
	new_matrix = [x[:] for x in matrix]
	for i in range(0, len(new_matrix)):
		for j in range(0, len(new_matrix[0])):
			new_matrix[i][j] = round(new_matrix[i][j] / div, 2)

	return (new_matrix)