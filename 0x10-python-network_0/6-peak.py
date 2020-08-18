#!/usr/bin/python3
"""
Finds peaks using python
"""


def find_peak(list_of_integers):
    """
    This function returns the peak of a list
    """
    if list_of_integers:
        return(max(set(list_of_integers)))
    return(None)
