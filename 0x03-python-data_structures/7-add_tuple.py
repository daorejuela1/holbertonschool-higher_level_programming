#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in range(0, 2):
        try:
            tuple_b[i]
        except:
            tuple_b = tuple_b + (0,)
    for i in range(0, 2):
        try:
            tuple_a[i]
        except:
            tuple_a = tuple_a + (0,)
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (result)
