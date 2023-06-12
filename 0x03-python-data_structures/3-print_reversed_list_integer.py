#!/usr/bin/python3
'''Print integers in reverse'''


def print_reversed_list_integer(my_list=[]):
    for num in range(len(my_list), 0, -1):
        print("{:d}".format(my_list[num - 1]))
