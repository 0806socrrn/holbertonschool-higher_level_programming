#!/usr/bin/python3
"""function that returns True if the object
 is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly of the class """

    if type(obj) is a_class:
        return True
    else:
        return False
