#!/usr/bin/python3
""" test for rectangle module"""
import unittest
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """testing for rectangle class"""
    
    def test_init(self):
        """testing for rectangle class initialize"""
        obj1 = Rectangle(10, 2)
        obj2 = Rectangle(2, 10, 7, 6)
        self.assertEqual(obj1.id, obj2.id - 1)
        self.assertEqual(obj2.id, obj1.id + 1)

        obj3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(obj3.id, 12)

        obj4 = Rectangle(10, 2, 7)
        self.assertEqual(obj4.id, obj1.id + 2)

        obj5 = Rectangle(4, 10)
        self.assertEqual(obj5.id, obj4.id + 1)

        obj6 = Rectangle(10, 2, 0, 0, 15)
        self.assertEqual(obj6.id, 15)

        obj7 = Rectangle(4, 10, 3)
        self.assertEqual(obj7.id, obj5.id + 1)

    def test_widthsetandget(self):
        """testing for rectangle class width"""
        self.assertRaises(TypeError, Rectangle, "10", 2)
        self.assertRaises(ValueError, Rectangle, -10, 2)

    def test_heightsetandget(self):
        """testing for rectangle class height"""
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(ValueError, Rectangle, 10, -2)

    def test_xsetandget(self):
        """testing for rectangle class x"""
        self.assertRaises(TypeError, Rectangle, 10, 2, {})
        self.assertRaises(ValueError, Rectangle, 10, 2, -3, 2)

    def test_ysetandget(self):
        """testing for rectangle class y"""
        self.assertRaises(TypeError, Rectangle, 10, 2, 4, {})
        self.assertRaises(ValueError, Rectangle, 10, 2, 5, -3)
    
    def test_area(self):
        """testing for rectangle class initialize"""
        obj8 = Rectangle(3, 2)
        self.assertEqual(obj8.area(), 6)

        obj9 = Rectangle(2, 10)
        self.assertEqual(obj9.area(), 20)

        obj10 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(obj10.area(), 56)

if __name__ == "__main__":
    unittest.main()
