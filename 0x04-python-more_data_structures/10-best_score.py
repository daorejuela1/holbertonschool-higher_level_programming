#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    max_value = list(a_dictionary.values())[0]
    for key in a_dictionary:
        if (a_dictionary[key] > max_value):
            max_value = a_dictionary[key]
            final_key = key
    return (final_key)
