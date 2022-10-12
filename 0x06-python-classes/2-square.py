#!/usr/bin/python3
"""defining a square class"""


class Square:
    """A blueprint for a square object"""
    def __init__(self, size=0):
        """size needs to be an integer and we need to check that"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
