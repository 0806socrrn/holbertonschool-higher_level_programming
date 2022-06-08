#!/usr/bin/python3
"""class that inherits `list` and adds a function to
print the list sorted in ascending order"""


class MyList(list):
    """kind of list with ordered impression"""


def print_sorted(self):
    """prints the list ascending"""

    print(sorted(self))
