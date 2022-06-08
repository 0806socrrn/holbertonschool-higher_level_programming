#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """opens the file and prints it to standard output"""
    with open(filename) as f:
        print(f.read(), end="")
