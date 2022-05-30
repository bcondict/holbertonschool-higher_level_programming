#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_normal(self):
    self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative(self):
    self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty(self):
    self.assertEqual(max_integer([]), None)

    def test_zero(self):
    self.assertEqual(max_integer([0]), 0)

    def test_float(self):
    self.assertEqual(max_integer([4.3, 2.4, 5.6, 1.2]), 5.6)

    def test_no_list(self):
        with self.assertRaises(TypeError):
            max_integer(1, 33, 5, 66)

    def test_dif_type(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'two', 3])

    def test_max_lett(self):
    self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')

    def test_max_string(self):
    self.assertEqual(max_integer(['Hello', 'Good', 'Bye']), 'Hello')

    def test_int_as_str(self):
    self.assertEqual(max_integer(['1', '2', '3']), '3')
