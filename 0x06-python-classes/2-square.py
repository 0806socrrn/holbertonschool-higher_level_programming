#!/usr/bin/python3
"""define a square based 1-square.py"""
class Square:
    def __init__(self, size=0):
        """defines the private distance attribute"""
        if (not isinstance(size, int)):
            """size whole number"""
            raise TypeError("size must be an integer")
        if (size < 0):
            """greater than zero"""
            raise TypeError("size must be >= 0")
        self.__size = size
