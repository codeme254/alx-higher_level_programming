#!/usr/bin/python3
"""defines a rectangle class and associated operations"""
from models.base import Base


class Rectangle(Base):
    """Blueprint for a rectangle and  operations"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the properties of the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """finds the area of a rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """Prints the rectangle instance with #"""
        for i in range(1, self.__height + 1):
            for j in range(1, self.__width + 1):
                print("#", end="")
            print("")
