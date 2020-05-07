#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    greater_than = lambda a, b: a if (a > b) else b
    max_value = 0
    for key in a_dictionary:
        max_value = greater_than(a_dictionary[key], max_value)
    return (max_value)
