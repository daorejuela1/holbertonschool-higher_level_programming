#!/usr/bin/python3
""" append after finding """


def append_after(filename="", search_string="", new_string=""):
    """This function appends text after finding text in a sequence"""
    with open(filename, 'r') as my_file:
        list_values = my_file.readlines()

    for i in range(len(list_values)):
        value = list_values[i].find(search_string)
        if (value != -1):
            list_values.insert(i + 1, new_string)

    with open(filename, 'w') as my_file:
        my_file.write("".join(list_values))
