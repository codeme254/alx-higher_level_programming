#!/usr/bin/python3
"""Writing to a text file and returning the number of characters written"""


def write_file(filename="", text=""):
    """Writes to a file and returns the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
