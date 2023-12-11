#!/usr/bin/python3
""" test for base module"""
import unittest
from models.base import Base


class Test_base(unittest.TestCase):
    """testing for base class"""
    
    def test_init(self):
        """testing for base class initialize"""
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        obj2 = Base()
        self.assertEqual(obj2.id, 2)

        obj3 = Base(15)
        self.assertEqual(obj3.id, 15)

        obj4 = Base()
        self.assertEqual(obj4.id, 3)

        obj5 = Base(None)
        self.assertEqual(obj5.id, 4)

if __name__ == "__main__":
    unittest.main()
