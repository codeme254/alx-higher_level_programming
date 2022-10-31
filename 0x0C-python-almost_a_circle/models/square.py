#!/usr/bin/python3
"""Defines a square class and it's associated operations"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The blueprint for a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square and some properties"""
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """Returns the print() and str() of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
