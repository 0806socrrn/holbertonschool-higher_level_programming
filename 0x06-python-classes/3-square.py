#!/usr/bin/python3
"""define a square based 3-square.py"""
class Square:
    """class Square"""
    def __init__(self, size=0):
        """defines the private distance attribute"""
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            """square with attributes size (int) that returns nothing"""
            raise TypeError("size must be >= 0")
        self.__size = size
    def area(self):
        """Public instance"""
        return self.__size ** 2
