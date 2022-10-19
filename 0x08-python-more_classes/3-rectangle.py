#!/usr/bin/python3

"""Defining a rectangle"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Gets the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Gets the perimeter of the rectangle
        if either width or height is 0, perimeter is 0"""
        width = self.__width
        height = self.__height

        if width == 0 or height == 0:
            return (0)
        else:
            return ((2*height)+(2*width))

    def __str__(self):
        """Graphically prints our rectangle using # symbol"""
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            print("")
        for i in range(1, height+1):
            for j in range(1, width+1):
                print("#", end="")
            print("")
        return ""
