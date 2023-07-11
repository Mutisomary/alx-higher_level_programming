#!/usr/bin/python3
"""Defines a text file reading function"""


def read_file(filename=""):
    """Prints contents of a file to the stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents)
