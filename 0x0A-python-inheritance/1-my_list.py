#!/usr/bin/python3
"""working with a class called MyList that does basic list stuffs"""


class MyList(list):
    """Defines a blueprint for a custom list
    It inherits from inbuilt list in python3"""
    def __init__(self):
        """Initializes the list"""
        super().__init__()

    def print_sorted(self):
        """prints a list sorted in ascending order"""
        print(sorted(self))
