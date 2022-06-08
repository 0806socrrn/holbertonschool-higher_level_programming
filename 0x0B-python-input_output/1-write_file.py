#!/usr/bin/python3
"""function that writes a string to a text file (UTF8) 
and returns the number of characters written"""

def number_of_lines(filename="", text=""):
    """This function returns the number of lines in a given file
    Args:
        filename (str): The name of the file to be analyzed
    Returns:
        int: The number of lines in the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)