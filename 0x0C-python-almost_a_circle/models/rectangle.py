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
        self.__width = new_data

    @height.setter
    def height(self, new_data):
        """
        Set height
        """
        self.__height = new_data

    @x.setter
    def x(self, new_data):
        """
        Set x
        """
        self.__x = new_data

    @y.setter
    def y(self, new_data):
        """
        Set y
        """
        self.__y = new_data
