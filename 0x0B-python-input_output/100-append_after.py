#!/usr/bin/python3
"""defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """inseert a text after each line"""
    text = ""
    with open(filename, "r") as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
