#!/usr/bin/python3
import unittest
import json
import os
from models.base import Base

"""Creating test class for Base module"""


class test_Base(unittest.TestCase):
    """Testing base"""

    def test_id_none(self):
        """no id sent"""
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        """valid id"""
        b = Base(10)
        self.assertEqual(10, b.id)

    def test_id_zero(self):
        """id is zero"""
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """id is negative"""
        b = Base(-10)
        self.assertEqual(-10, b.id)

    def test_id_list(self):
        """id is a list"""
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        """ id is a dictionary"""
        b = Base({"id": 10})
        self.assertEqual({"id": 10}, b.id)

    def test_id_tuple(self):
        """id is a tuple"""
        b = Base((1, 2, 3,))
        self.assertEqual((1, 2, 3,), b.id)

    def test_id_string(self):
        """id is a string"""
        b = Base("Mary")
        self.assertEqual("Mary", b.id)


if __name__ == '__main__':
    unittest.main()
