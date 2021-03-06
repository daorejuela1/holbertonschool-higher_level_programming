#!/usr/bin/python3
"""
Finds peaks using python
"""


def find_peak(list_of_integers):
    """
    This function returns the peak of a list
    """
    if list_of_integers:
        if(list_of_integers[0] > list_of_integers[1]):
            return list_of_integers[0]
        elif(list_of_integers[-1] > list_of_integers[-2]):
            return list_of_integers[-1]
        else:
            return(max(list_of_integers))
    return(None)
