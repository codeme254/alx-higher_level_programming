#!/usr/bin/python3
"""appending string to the end of a file and return the number of characters"""


def append_write(filename="", text=""):
    """Appends string to the end of a file, returns no. of characters added"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
