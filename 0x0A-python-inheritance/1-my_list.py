#!/usr/bin/python3
"""
Here we use python inheritance with a list object
"""


class MyList(list):
    """
    This class mimics the list behavior with
    a new component
    """

    def __init__(self):
        """
        Init Mylist with list params
        """
        list.__init__(self)

    def print_sorted(self):
        """
        Prints the list in sorted order
        """
        my_list = self
        print(sorted(my_list))
