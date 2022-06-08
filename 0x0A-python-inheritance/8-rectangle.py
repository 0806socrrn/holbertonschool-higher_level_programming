#!/usr/bin/python3
"""class BaseGeometry (based on 5-base_geometry.py)."""


class BaseGeometry:
    """geometry class"""

    def area(self):
        """instance method"""
        raise Exception("area() is not implemented")


def __init__(self, width, height):
    """Init function with width and height"""

    try:
        self.integer_validator("width", width)
    except Exception as e:
        raise
    else:
        self.__width = width

    try:
        self.integer_validator("height", height)
    except Exception as e:
        raise
    else:
        self.__height = height
