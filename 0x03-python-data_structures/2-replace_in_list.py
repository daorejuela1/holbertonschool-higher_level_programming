#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace element in list, if not found returns None"""
    if (idx + 1 > len(my_list) or idx < 0):
        return (my_list)
    else:
        my_list[idx] = element
        return(my_list)
