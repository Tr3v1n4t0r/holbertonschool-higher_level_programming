#!/usr/bin/python3
"""
Module for testing the Base class
"""
import contextlib
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO

class TestClassBase(unittest.TestCase):
    """Test the Base class"""

    def setUp(self):
        """Sets up base class"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Finishing after test methods"""
        pass

    def test_init(self):
        """Tests proper init"""
        a = Base()
        b = Base(12)
        self.assertEqual(type(a), Base)
        self.assertEqual(type(b), Base)

    def test_type(self):
        """Tests type"""
        a = Base()
        self.assertTrue(type(a) == Base)

    def test_id(self):
        """Tests id"""
        a = Base()
        b = Base(12)
        c = Base(-28)
        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 12)
        self.assertEqual(c.id, -28)

    def test_unknown(self):
        """Tests name error"""
        with self.assertRaises(NameError):
            Base(a)

    def test_empty_json(self):
        """Tests to_json_string method with empty and None"""
        json = Base.to_json_string('')
        self.assertEqual(json, '[]')
        json = Base.to_json_string(None)
        self.assertEqual(json, '[]')

    def test_json(self):
        """Tests to_json_string method"""
        a = Rectangle(12, 3, 9, 2)
        dictionary = a.to_dictionary()
        json = Base.to_json_string([dictionary])
        self.assertEqual(len(json), len(str([{"x": 9, "width": 12, "id": 1,
                                              "height": 3, "y": 2}])))
        self.assertTrue(type(json), dict)
        self.assertTrue(type(json) is str)

if __name__ == '__main__':
    unittest.main()
