#!/usr/bin/python3
"""implementing a square class that inherits from a rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Blueprint for a square shape/figure"""
    def __init__(self, size):
        """initializing the properties of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size
