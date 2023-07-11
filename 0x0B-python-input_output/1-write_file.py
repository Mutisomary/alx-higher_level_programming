#!/usr/bin/python3
"""Define a file writing fucntion"""


def write_file(filename="", text=""):
    """write a string to stdout"""
    with open(filename, "w") as f:
        return f.write(text)
