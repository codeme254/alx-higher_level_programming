#!/usr/bin/python3

"""Defines an integer addition"""


def add_integer(a, b=98):
    """ Adds two digits a and b and returns the result
    these two digits should be of float or int data type
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b
