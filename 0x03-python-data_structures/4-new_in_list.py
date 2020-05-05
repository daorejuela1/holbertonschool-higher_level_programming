#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace element and return a new list"""
    if (idx + 1 > len(my_list) or idx < 0):
        return(my_list)
    else:
        backup_list = my_list.copy()
        backup_list[idx] = element
        return(backup_list)
