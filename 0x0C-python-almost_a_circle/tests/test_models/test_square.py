#!/usr/bin/python3
""" unittest for Square class"""

import unittest
import json

from models.base import Base

from models import square

from io import StringIO
from unittest.mock import patch

Square = square.Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def testModuleDoc(self):
        self.assertTrue(square.__doc__)

    def testClassDoc(self):
        self.assertTrue(Square.__doc__)


if __name__ == '__main__':
    unittest.main()
