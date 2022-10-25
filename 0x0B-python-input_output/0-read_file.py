#!/usr/bin/python3
"""Reading a text file and printing its content it to the standard output"""


def read_file(filename=""):
    """Reads file content and print it to the standard output"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
