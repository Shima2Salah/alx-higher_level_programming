#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for maximum integer number"""

    def test_description(self):
        """Test for positive integers"""
        self.assertEqual(max_integer([7, 9, 3, 4]), 9)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        
    def test_description(self):
        """Test with none results"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)

    def test_description(self):
        """Test for negative integers"""
        self.assertEqual(max_integer([-7, -9, 3, 4]), 4)
        
    def test_string(self):
        """Test for negative integers"""
        self.assertEqual(max_integer("Clexane"), "x")
