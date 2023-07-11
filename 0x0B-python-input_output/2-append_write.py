#!/usr/bin/python3
"""defining a string append function"""


def append_write(filename="", text=""):
    """append a string at the end of a text"""
    with open(filename, "a") as f:
        return f.write(text)
