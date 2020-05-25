#!/usr/bin/python3
""" This script solves the N-Queen problem"""
import sys


def put_coords(matrix, result):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if (matrix[i][j] == 1):
                result[i][0] = i
                result[i][1] = j
    return result


def check_moves(matrix, position_x, position_y):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            # Si hay un 1 horizontal
            if (matrix[x][position_y] == 1):
                return(1)
            # Si hay un 1 vertical
            if (matrix[position_x][y] == 1):
                return(1)
            # Si hay un 1 diagonal abajo a la derecha
            try:
                if (matrix[position_x + x][position_y + x] == 1):
                    return(1)
            except IndexError:
                pass
            try:
                if (position_x - x >= 0):
                    if (matrix[position_x - x][position_y + x] == 1):
                        return(1)
            except IndexError:
                pass
            try:
                if (position_x - x >= 0 and position_y - x >= 0):
                    if (matrix[position_x - x][position_y - x] == 1):
                        return(1)
            except IndexError:
                pass
            try:
                if (position_y - x >= 0):
                    if (matrix[position_x + x][position_y - x] == 1):
                        return(1)
            except IndexError:
                pass
    return(0)

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
n = int(sys.argv[1])
if type(n) is not int:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

matrix = [[0 for x in range(n)] for y in range(n)]
result = [[0 for x in range(2)] for y in range(n)]
row = 1
king = 0
while(king != n - 1):
    matrix[0][king] = 1
    for column in range(n):
        if (check_moves(matrix, row, column) == 0):
            matrix[row][column] = 1
            if (row == n - 1):
                put_coords(matrix, result)
                print(result)
            if (row < n - 1):
                row = row + 1
        elif (column == n - 1):
            matrix = [[0 for x in range(n)] for y in range(n)]
            king = king + 1
            row = 1
