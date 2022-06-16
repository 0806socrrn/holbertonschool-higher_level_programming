#!/usr/bin/python3
"""
Base Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get width
        """
        return self.__width

    @property
    def height(self):
        """
        Get height
        """
        return self.__height

    @property
    def x(self):
        """
        Get x
        """
        return self.__x

    @property
    def y(self):
        """
        Get y
        """
        return self.__y

    @width.setter
    def width(self, new_data):
        """
        Set width
        """
        if type(new_data) is not int:
            raise TypeError("width must be an integer")
        if new_data <= 0:
            raise TypeError("width must be > 0")
        self.__width = new_data

    @height.setter
    def height(self, new_data):
        """
        Set height
        """
        if type(new_data) is not int:
            raise TypeError("height must be an integer")
        if new_data <= 0:
            raise TypeError("height must be > 0")
        self.__height = new_data

    @x.setter
    def x(self, new_data):
        """
        Set x
        """
        if type(new_data) is not int:
            raise TypeError("x must be an integer")
        if new_data < 0:
            raise TypeError("x must be >= 0")
        self.__x = new_data

    @y.setter
    def y(self, new_data):
        """
        Set y
        """
        if type(new_data) is not int:
            raise TypeError("y must be an integer")
        if new_data < 0:
            raise TypeError("y must be >= 0")
        self.__y = new_data

    def area(self):
        """
        Area
        """
        return(self.width * self.height)
