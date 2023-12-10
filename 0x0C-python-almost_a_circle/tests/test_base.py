#!/usr/bin/python3
""" test for base module"""
import unittest:


class Test_base(unittest.TestCase):
    """testing for base class"""
    
    def test_init(self):
        """testing for base class initialize"""
        self.assertequal(Base(), 1)
        self.assertequal(Base(), 2)
        self.assertequal(Base(15), 15)
        self.assertequal(Base(), 3)
        self.assertequal(Base(None), 4)

if __name__ == "__main__":
    unittest.main()
