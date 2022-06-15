#!/usr/bin/python3
""" unittest for Square class"""

from re import S
from typing import Type
import unittest
import json

from models.base import Base

from models import square

from io import StringIO
from unittest.mock import patch

Square = square.Square


class TestSquare(unittest.TestCase):
    """test Square class"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def testModuleDoc(self):
        """test if Square module is documented"""
        self.assertTrue(square.__doc__)

    def testClassDoc(self):
        """test if Square class is documented"""
        self.assertTrue(Square.__doc__)

    def testNormal(self):
        """test normal size Square"""
        s1 = Square(2)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def testComplete(self):
        """test size complete instance"""
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 4)

    def testNoArgs(self):
        """test error no arguments"""
        with self.assertRaises(TypeError):
            s1 = Square()

    def testStr(self):
        """test string values"""
        with self.assertRaises(TypeError):
            s1 = Square("1")

    def testFloat(self):
        """test float values"""
        with self.assertRaises(TypeError):
            s1 = Square("2.5")

    def testZeroValue(self):
        """test 0 values"""
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def testNegValue(self):
        """test negative values"""
        with self.assertRaises(ValueError):
            s1 = Square(-1)

    def testReplaceValues(self):
        """test replace values"""
        s1 = Square(1, 2, 3, 4)
        s1.id = 1
        s1.y = 2
        s1.x = 3
        s1.size = 4
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 1)

    def testArea(self):
        """testing area"""
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)

    def testAreaArgs(self):
        """test error passing area arguments"""
        s1 = Square(2)
        with self.assertRaises(TypeError):
            area = s1.area(2)

    def testDisplay(self):
        """test std output for Square representation"""
        s1 = Square(2)
        output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as f:
            s1.display()
            self.assertEqual(f.getvalue(), output)

    def testDisplayComplete(self):
        """test std output for square complete instance representation"""
        s1 = Square(3, 2, 1)
        output = "\n  ###\n  ###\n  ###\n"
        with patch('sys.stdout', new=StringIO()) as f:
            s1.display()
            self.assertEqual(f.getvalue(), output)

    def tesr_Str_StdOutput(self):
        """test std output for str method"""
        s1 = Square(1, 2, 3, 4)
        output = "[Square] (4) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as f:
            print(s1)
            self.assertEqual(f.getvalue(), output)

    def test_str_Normal(self):
        """test str method"""
        s1 = Square(1, 2, 3, 4)
        output = "[Square] (4) 2/3 - 1"
        self.assertAlmostEqual(s1.__str__(), output)

    def testUpdate(self):
        """test update to change square values"""
        s1 = Square(1, 2, 3, 4)
        output = "[Square] (4) 2/3 - 1"
        self.assertAlmostEqual(s1.__str__(), output)

        s1 = Square(4, 3, 2, 1)
        output = "[Square] (1) 3/2 - 4"
        self.assertAlmostEqual(s1.__str__(), output)

    def testUpdateNone(self):
        """test error None values to change"""
        s1 = Square(1, 2)
        self.assertFalse(s1.update())

    def testUpdateKW(self):
        """test key words values to change"""
        s1 = Square(1, 2)
        s1.update(id=3, x=2, y=1)
        self.assertEqual(s1.id, 3)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 1)

    def testUpdateMix(self):
        """test with mixed args and kwargs"""
        s1 = Square(1)
        self.assertFalse(s1.update(1, x=3, y=4, id=5))

    def testTo_Dictionary(self):
        """test normal use for to_dictionary method"""
        s1 = Square(1, 2, 3, 4)
        s1_dict = s1.to_dictionary()
        output = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertIsInstance(s1_dict, dict)
        self.assertDictEqual(s1_dict, output)


if __name__ == '__main__':
    unittest.main()
