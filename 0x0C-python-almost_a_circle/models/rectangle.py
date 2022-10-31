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
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """Gets the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        self.__x = value

    @property
    def y(self):
        """gets the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        self.__y = value
