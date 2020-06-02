#!/usr/bin/python3
"""
Starting module to define base geometry class
"""


class BaseGeometry():
    """"
    Template for a base geometry object
    """
    def __init__(self):
        """ Initial constructor space """
        pass

    def area(self):
        """ Space to calculate the area (in progress) """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer number """
        if (type(value) is not int):
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
