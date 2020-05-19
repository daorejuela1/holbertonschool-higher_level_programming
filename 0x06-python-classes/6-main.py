#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(0)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (5, 7))
my_square_2.position = (0,0)
my_square_2.my_print()

print("--")

my_square_3 = Square(5, (0, 0))
my_square_3.my_print()

print("--")

