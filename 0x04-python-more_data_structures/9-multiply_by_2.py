#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    power_2 = lambda x: x * 2
    for key in a_dictionary:
        new_dict[key] = power_2(a_dictionary[key])
    return (new_dict)
