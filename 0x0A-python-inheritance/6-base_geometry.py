#!/usr/bin/python3
"""Defines a geometry module"""


class BaseGeometry:
    """Blueprint for the geometry"""

    def area(self):
        """supposed to find the area of something"""
        raise Exception("area() is not implemented")
