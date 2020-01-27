#!/usr/bin/python3
"""
Module for testing the Base class
"""
import unittest
from models.base import Base

class TestClassBase(unittest.TestCase):
    """Test the Base class"""

    def test_init(self):
        """Tests proper init"""
        a = Base()
        b = Base(12)
        self.assertEqual(type(a), Base)
        self.assertEqual(type(b), Base)

    def test_id(self):
        a = Base()
        b = Base()
        c = Base(2)
        d = Base(50)
        e = Base(-2)
        f = Base(-50)
        self.asserEqual(a.id, 1)
        self.asserEqual(b.id, 2)
        self.asserEqual(c.id, 3)
        self.asserEqual(d.id, 50)
        self.asserEqual(e.id, -2)
        self.asserEqual(f.id, -50)

    def test_type(self):
        a = Base()
        self.assertTrue(type(a) == Base)

if __name__ == '__main__':
    unittest.main()
