#!/usr/bin/python3
def no_c(my_string):
    """Eliminates all cC characters in a string"""
    current_list = list(my_string)
    max = len(current_list)

    for character in range(0, max):
        try:
            if current_list[character] == 'c' or current_list[character] == 'C':
                del current_list[character]
        except IndexError:
            pass
    output_string = ''.join(current_list)
    return output_string
