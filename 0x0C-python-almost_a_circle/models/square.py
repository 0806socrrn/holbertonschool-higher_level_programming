#!/usr/bin/python3
"""
Base Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Prints the square details
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """
        Get size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Set size
        """
        self.width = size
        self.height = size
