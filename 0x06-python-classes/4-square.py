#!/usr/bin/python3
"""Defining a square class with getter and setter both named size"""


class Square:
    """A blueprint for a square object"""
    def __init__(self, size=0):
        """size needs to be an integer and we need to check that"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter method to get the size of the squre"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size
