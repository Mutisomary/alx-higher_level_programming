#!/usr/bin/python3

def no_c(my_string):
     copy = [num for num in my_string if num != 'c' and num != 'C']
     return ("".join(copy))
