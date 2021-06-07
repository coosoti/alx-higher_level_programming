#!/usr/bin/python3
"""unittest for Rectangle class module"""


import unittest
from models.base import Base
from models import rectangle
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """unittest for the Rectangle class"""

    def test_module_doc(self):
        self.assertTrue(len(rectangle.__doc__) > 0)

    def test_class_doc(self):
        self.assertTrue(len(Rectangle.__doc__) > 0)


if __name__ == '__main__':
    unittest.main()
