#!/usr/bin/python3
import unittest
import json
import os
from models.square import Square
import inspect
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
        b = Base((8,))
        self.assertEqual((8,), b.id)

    def test_id_string(self):
        """Sending an id that is not an int"""
        b = Base("Mary")
        self.assertEqual("Mary", b.id)

    def test_to_json_type(self):
        '''
            Testing the json string
        '''
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


class TestSquare(unittest.TestCase):
    """
    class for testing Base class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
