#!/usr/bin/python3
"""Base class for all the other classes in this project"""


class Base:
    """Blueprint for Base, parent class for all the other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base class, parent class for other classes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
