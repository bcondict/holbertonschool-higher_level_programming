#!/usr/bin/python3
""" unittest for Rectangle class"""

import unittest
import json

from models.base import Base
from models import rectangle

from io import StringIO
from unittest.mock import patch

Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """test Rectangle class"""
    def setUp(self):
        """star fo every test"""
        Base._Base__nb_objects = 0

    def testModuleDoc(self):
        """test if rectangle module is documented"""
        self.assertTrue(rectangle.__doc__)

    def testClassDoc(self):
        """test if rectangle class is documented"""
        self.assertTrue(Rectangle.__doc__)

    def testWidth_Height(self):
        """test normal width and height rectangle"""
        r1 = Rectangle(1, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def testComplete(self):
        """test rectangle complete instance"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)

    def testIncomplete(self):
        """test error too few arguments"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def testStringValue(self):
        """test string values"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, "1")

    def testZeroValue(self):
        """test 0 values"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 0)

    def testNegativeValues(self):
        """test negatives values"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, -1)

    def testReplaceValues(self):
        """test replace values"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.id = 1
        r1.y = 2
        r1.x = 3
        r1.height = 4
        r1.width = 5
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 1)

    def testArea(self):
        """testing area"""
        r1 = Rectangle(3, 4)
        area = r1.area()
        self.assertEqual(area, 12)

    def testAreaArgs(self):
        """test error passing area arguments"""
        r1 = Rectangle(3, 4)
        with self.assertRaises(TypeError):
            area = r1.area(5)

    def testDisplay(self):
        """test std output for rectangle representation"""
        r1 = Rectangle(3, 4)
        output = "###\n###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as f:
            r1.display()
            self.assertEqual(f.getvalue(), output)

    def testDisplayComplete(self):
        """test std output for rectangle complete instance representation"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        output = "\n\n\n\n   #\n   #\n"
        with patch('sys.stdout', new=StringIO()) as f:
            r1.display()
            self.assertEqual(f.getvalue(), output)

    def tesr_Str_StdOutput(self):
        """test std output for str method"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        output = "[Rectangle] (5) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as f:
            print(r1)
            self.assertEqual(f.getvalue(), output)

    def test_str_Normal(self):
        """test str method"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        output = "[Rectangle] (5) 3/4 - 1/2"
        self.assertAlmostEqual(r1.__str__(), output)

    def testUpdate(self):
        """test update to change rectangle values"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        output = "[Rectangle] (5) 3/4 - 1/2"
        self.assertAlmostEqual(r1.__str__(), output)

        r1.update(5, 4, 3, 2, 1)
        output = "[Rectangle] (5) 2/1 - 4/3"
        self.assertAlmostEqual(r1.__str__(), output)

    def testUpdateNone(self):
        """test error None values to change"""
        r1 = Rectangle(1, 2)
        self.assertFalse(r1.update())

    def testUpdateKW(self):
        """test key words values to change"""
        r1 = Rectangle(1, 2)
        r1.update(id=3, x=2, y=1)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)


if __name__ == '__main__':
    unittest.main()
