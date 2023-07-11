#!/usr/bin/python3
"""Defining a text reading function"""


def read_file(filename=""):
    """Print te contents of a file to the stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
