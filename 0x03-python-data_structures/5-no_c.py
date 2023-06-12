#!/usr/bin/python3


def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [num for num in my_string if num != 'c' and num != 'C']
    return ("".join(copy))
