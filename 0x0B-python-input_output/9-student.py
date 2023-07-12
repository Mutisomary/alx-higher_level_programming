#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represent Student"""
    def __init__(self, first_name, last_name, age):
        """initialize a new student"""
        self.first_name = first_name
        self.last_name =  last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation"""
        return self.__dict__
