#!/usr/bin/python3
"""function that writes a string to a text file (UTF8) 
and returns the number of characters written"""


def write_file(filename="", text=""):
    """This function writes
    filename: file to wirte to"""

    with open(filename, "r") as f:
        return sum(1 for x in f)
