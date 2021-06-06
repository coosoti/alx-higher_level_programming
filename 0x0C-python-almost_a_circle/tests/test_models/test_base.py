#!/usr/bin/python3
"""Unittest for the Base class"""


import unittest
from models import base
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """unittest class for the Base class"""

    def test_documentation(self):
        """Test documentation"""

        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """Test documentation"""

        self.assertTrue(len(Base.__doc__) > 0)

    def test_id(self):
        """Test ids"""

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

if __name__ == '__main__':
    unittest.main()
