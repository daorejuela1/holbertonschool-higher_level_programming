#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """Reads line by line till n.

    Args:
        filename: path to the file that wants to be read.
        nb_lines: number of lines to be read

    Returns:
        Nothing.

    """
    counter = 0
    with open(filename, "r") as my_file:
        for line in my_file:
            counter += 1
            print(line, end = "")
            if counter == nb_lines:
                break
    my_file.close()
    return (counter)