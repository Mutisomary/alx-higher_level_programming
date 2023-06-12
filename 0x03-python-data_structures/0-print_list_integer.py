#!/usr/bin/python3
'''print integers in a list'''
def print_list_integer(my_list=[]):
    for num in range(len(my_list)):
        print("{:d}".format(my_list[num]))
