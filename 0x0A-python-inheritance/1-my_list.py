#!/usr/bin/python3

"""MyList class module"""


class MyList(list):
    """defines a subclass MyList"""

    def __init__(self):
        """initialize the constructor"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
