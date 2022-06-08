#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry 
(7-base_geometry.py)."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Basic rectangle function"""

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
