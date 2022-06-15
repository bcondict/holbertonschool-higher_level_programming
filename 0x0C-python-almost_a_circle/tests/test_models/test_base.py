#!/usr/bin/python3
""" unittest for Base class"""

import unittest
import json

from models import base
from models.rectangle import Rectangle
from models.square import Square

Base = base.Base


class TestBase(unittest.TestCase):
    """tase for base class"""
    def setUp(self):
        """star fo every test"""
        Base._Base__nb_objects = 0

    def testModuleDoc(self):
        """test if rectangle module is documented"""
        self.assertTrue(base.__doc__)

    def testClassDoc(self):
        """test if rectangle class is documented"""
        self.assertTrue(Base.__doc__)

    def testNormal(self):
        """test normal id set default 1"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def testMoreNormal(self):
        """test normal id increases in 1"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def testGivenId(self):
        """test with a given id"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def testStringId(self):
        """test string number id """
        b1 = Base("12")
        self.assertEqual(b1.id, "12")

    def testTwoNum(self):
        """test more than 1 given number"""
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)

    def testTo_Json_String(self):
        """test to change a dictionary to json file"""
        r1 = Rectangle(1, 2, 3, 4)
        dic1 = r1.to_dictionary()
        json_dic = Base.to_json_string([dic1])
        dic_json = json.loads(json_dic)
        self.assertEqual(dic_json, [dic1])

    def testSave_To_fileNoArg(self):
        """test error no something to save into json file"""
        s1 = Square(1)
        with self.assertRaises(TypeError):
            s1.save_to_file()

    def testSave_To_fileMoreArgs(self):
        """test error given more then needed to save into json file"""
        r1 = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r1.save_to_file([r1], [])

    def testFrom_Json_to_string(self):
        """test normal use for from_json_string method"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertIsInstance(list_output, list)
        self.assertIsInstance(list_output[0], dict)
        self.assertIsInstance(list_output[1], dict)

    def testFrom_Json_to_stringEmpty(self):
        """test no given something to save"""
        with self.assertRaises(TypeError):
            list_output = Base.from_json_string()

    def testCreate(self):
        """normal use for create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r2, Rectangle)

    def testCreateMoreArgs(self):
        """test create method with more needed argument"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(3, 6, 2)
        r2_dictionary = r2.to_dictionary()
        with self.assertRaises(TypeError):
            r3 = Base.create(**r1_dictionary, **r1_dictionary)

    def testCreateNoDic(self):
        """test create method with no given dictionary"""
        r1 = Rectangle(3, 5, 1)
        with self.assertRaises(TypeError):
            r2 = Base.create(r1)


if __name__ == '__main__':
    unittest.main()
