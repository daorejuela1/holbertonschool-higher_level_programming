#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    max_value = list(a_dictionary.values())[0]
    for key in a_dictionary:
        max_value = greater_than(a_dictionary[key], max_value)
    return (max_value)


def greater_than(a, b):
    if (a > b):
        return (a)
    else:
        return (b)
