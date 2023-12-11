#!/usr/bin/python3
""" test for rectangle module"""
import unittest
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """testing for rectangle class"""
    
    def test_init(self):
        """testing for rectangle class initialize"""
        obj1 = Rectangle(10, 2)
        self.assertEqual(obj1.id, 1)

        obj2 = Rectangle(2, 10, 7, 6)
        self.assertEqual(obj2.id, 2)

        obj3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(obj3.id, 12)

        obj4 = Rectangle(10, 2, 7)
        self.assertEqual(obj4.id, 3)

        obj5 = Rectangle(4, 10)
        self.assertEqual(obj5.id, 4)

        obj6 = Rectangle(10, 2, 0, 0, 15)
        self.assertEqual(obj6.id, 15)

        obj7 = Rectangle(4, 10, 3)
        self.assertEqual(obj7.id, 5)

if __name__ == "__main__":
    unittest.main()
