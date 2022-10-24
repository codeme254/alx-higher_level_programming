#!/usr/bin/python3
"""returns True if an object is exactly an instance of a class"""


def is_same_class(obj, a_class):
    """Returns true if obj is exactly an instance of a_class"""
    if type(obj) == a_class:
        return True
    return False
