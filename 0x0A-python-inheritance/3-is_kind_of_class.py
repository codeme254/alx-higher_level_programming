#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """returns True if obj is an instance of or if obj is an instance
    of a class that it inherited from"""
    return isinstance(obj, a_class)
