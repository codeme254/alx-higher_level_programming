#!/usr/bin/python3
"""Defines a geometry module"""


class BaseGeometry:
    """Blueprint for the geometry"""

    def area(self):
        """supposed to find the area of something"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates name against value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
