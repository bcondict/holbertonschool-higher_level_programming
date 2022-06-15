#!/usr/bin/python3
""" unittest for Square class"""

import unittest
import json

from models.base import Base
from models import rectangle

from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def testModuleDoc(self):
        self.assertTrue(rectangle.__doc__)

    def testClassDoc(self):
        self.assertTrue(Rectangle.__doc__)


if __name__ == '__main__':
    unittest.main()
