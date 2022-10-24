#!/usr/bin/python3
"""only subclass of"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
    (directly or indirectly) a_class, otherwise, False"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
