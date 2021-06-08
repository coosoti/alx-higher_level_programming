#!/usr/bin/python3
"""Unittest for the Square class"""


import unittest
import inspect
from models import square
from models.base import Base
from models.square import Square
from contextlib import redirect_stdout
import io
import json
import os


class TestSquareDocstrings(unittest.TestCase):
    """Unittests for the Square class documentation"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.square_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_module_docstring(self):
        """Tests for existence of a module docstring"""
        self.assertTrue(len(square.__doc__) > 0)

    def test_class_docstring(self):
        """Tests for the existence of a class docstring"""
        self.assertTrue(len(Square.__doc__) > 0)

    def test_func_docstrings(self):
        """Tests for the existence of docstrings in all functions"""
        for func in self.square_funcs:
            self.assertTrue(len(func[1].__doc__) > 0)


class TestSquare(unittest.TestCase):
    """Tests for the Square class"""
    @classmethod
    def setUpClass(cls):
        """set up the tests"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)
        cls.s3 = Square(4, 5, 6)
        cls.s4 = Square(7, 8, 9, 10)

    def test_instance_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 10)

    def test_size(self):
        """Test for functioning size"""
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 4)
        self.assertEqual(self.s4.size, 7)

    def test_width(self):
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s3.width, 4)
        self.assertEqual(self.s4.width, 7)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s3.height, 4)
        self.assertEqual(self.s4.height, 7)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s3.x, 5)
        self.assertEqual(self.s4.x, 8)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 9)

    def test_mandatory_size(self):
        """Test that width is a mandatory argument"""
        with self.assertRaises(TypeError):
            sq = Square()

    def test_size_typeerror(self):
        """Test that non-integers for size raise typerrors"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq = Square("osoti")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq = Square(True)

    def test_x_typeerror(self):
        """Test that non-integers for x raise typeerror"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq = Square(1, "osoti")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq = Square(1, True)

    def test_y_typeerror(self):
        """Test that non-integers for y raise typeerror"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq = Square(1, 1, "kulundeng")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq = Square(1, 1, True)

    def test_size_valueerror(self):
        """Test that negative integers size < 0 for size raise ValueError"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq = Square(0)

    def test_x_valueerror(self):
        """Test that negative integers x < 0 for x raise ValueErrror"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq = Square(1, -1)

    def test_y_valueerror(self):
        """Test that negative integer y < 0 for y raise valueerror"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq = Square(1, 1, -1)

    def test_area(self):
        """test that area is calculate appropriately"""
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 16)
        self.assertEqual(self.s4.area(), 49)

    def test_area_args(self):
        """Test too many args for area()"""
        with self.assertRaises(TypeError):
            a = self.s1.area(1)

    def test_basic_display(self):
        """Test display without x and y"""
        sq = Square(3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.s1.display()
            output = buf.getvalue()
            self.assertEqual(output, "#\n")
        with io.StringIO() as buf, redirect_stdout(buf):
            sq.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 3 + "\n") * 3)

    def test_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.s1.display(1)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.s2), "[Square] (2) 3/0 - 2")
        self.assertEqual(str(self.s3), "[Square] (3) 5/6 - 4")
        self.assertEqual(str(self.s4), "[Square] (10) 8/9 - 7")

    def test_display_xy(self):
        """Testing the display method with x and y"""
        with io.StringIO() as buf, redirect_stdout(buf):
            self.s2.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 3 + "#" * 2 + "\n") * 2)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.s3.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 6 +
                             (" " * 5 + "#" * 4 + "\n") * 4)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.s4.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 9 +
                             (" " * 8 + "#" * 7 + "\n") * 7)

    def test_update_args(self):
        """Testing the udpate method with *args"""
        sq = Square(1, 0, 0, 1)
        self.assertEqual(str(sq), "[Square] (1) 0/0 - 1")
        sq.update(89)
        self.assertEqual(str(sq), "[Square] (89) 0/0 - 1")
        sq.update(89, 2)
        self.assertEqual(str(sq), "[Square] (89) 0/0 - 2")
        sq.update(89, 2, 3)
        self.assertEqual(str(sq), "[Square] (89) 3/0 - 2")
        sq.update(89, 2, 3, 4)
        self.assertEqual(str(sq), "[Square] (89) 3/4 - 2")

    def test_update_args_setter(self):
        """tests that the update method uses setter with *args"""
        sq = Square(1, 0, 0, 1)
        with self.assertRaises(TypeError):
            sq.update(1, "kulundeng")
        with self.assertRaises(TypeError):
            sq.update(1, 1, "kulundeng")
        with self.assertRaises(TypeError):
            sq.update(1, 1, 1, "kulundeng")
        with self.assertRaises(ValueError):
            sq.update(1, 0)
        with self.assertRaises(ValueError):
            sq.update(1, -1)
        with self.assertRaises(ValueError):
            sq.update(1, 1, -1)
        with self.assertRaises(ValueError):
            sq.update(1, 1, 1, -1)

    def test_update_too_many_args(self):
        """test too many args for update"""
        sq = Square(1, 0, 0, 1)
        sq.update(1, 1, 1, 1, 2)
        self.assertEqual(str(sq), "[Square] (1) 1/1 - 1")

    def test_update_no_args(self):
        """test no args for update"""
        sq = Square(1, 0, 0, 1)
        sq.update()
        self.assertEqual(str(sq), "[Square] (1) 0/0 - 1")

    def test_update_kwargs(self):
        """Testing the update method with **kwargs"""
        sq = Square(1, 0, 0, 1)
        self.assertEqual(str(sq), "[Square] (1) 0/0 - 1")
        sq.update(size=10)
        self.assertEqual(str(sq), "[Square] (1) 0/0 - 10")
        sq.update(size=11, x=2)
        self.assertEqual(str(sq), "[Square] (1) 2/0 - 11")
        sq.update(y=3, size=4, x=5, id=89)
        self.assertEqual(str(sq), "[Square] (89) 5/3 - 4")

    def test_update_kwargs_setter(self):
        """tests that the update method uses setter with **kwargs"""
        sq = Square(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            sq.update(size="icampus")
        with self.assertRaises(TypeError):
            sq.update(x="icampus")
        with self.assertRaises(TypeError):
            sq.update(y="huhuh")
        with self.assertRaises(ValueError):
            sq.update(size=-1)
        with self.assertRaises(ValueError):
            sq.update(size=0)
        with self.assertRaises(ValueError):
            sq.update(x=-1)
        with self.assertRaises(ValueError):
            sq.update(y=-1)

    def test_mix_args_kwargs(self):
        """tests output for mixed args and kwargs"""
        sq = Square(1, 0, 0, 1)
        sq.update(2, 2, 2, 2, size=3, x=3, y=3, id=3)
        self.assertEqual(str(sq), "[Square] (2) 2/2 - 2")

    def test_extra_kwargs(self):
        """tests for random kwargs"""
        sq = Square(1, 0, 0, 1)
        sq.update(kulundeng=2)
        self.assertEqual(str(sq), "[Square] (1) 0/0 - 1")

    def test_to_dict(self):
        """test regular to_dictionary"""
        dict1 = self.s1.to_dictionary()
        self.assertEqual({"id": 1, "size": 1, "x": 0, "y": 0}, dict1)
        dict2 = self.s2.to_dictionary()
        self.assertEqual({"id": 2, "size": 2, "x": 3, "y": 0}, dict2)
        dict3 = self.s3.to_dictionary()
        self.assertEqual({"id": 3, "size": 4, "x": 5, "y": 6}, dict3)
        dict4 = self.s4.to_dictionary()
        self.assertEqual({"id": 10, "size": 7, "x": 8, "y": 9}, dict4)
        self.assertTrue(type(dict1) is dict)
        self.assertTrue(type(dict2) is dict)
        self.assertTrue(type(dict3)is dict)
        self.assertTrue(type(dict4) is dict)
        sq = Square(1, 1, 1, 1)
        sq.update(**dict4)
        self.assertEqual(str(sq), str(self.s4))
        self.assertNotEqual(sq, self.s4)

    def test_save_to_file(self):
        """test regular use of save_to_file"""
        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        l = [s1, s2]
        Square.save_to_file(l)
        with open("Square.json", "r") as f:
            ls = [s1.to_dictionary(), s2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_stf_empty(self):
        """test save_to_file with empty list"""
        l = []
        Square.save_to_file(l)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_stf_None(self):
        """test save_to_file with None"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_create(self):
        """test normal use of create"""
        s1 = {"id": 2, "size": 3, "x": 4, "y": 0}
        s2 = {"id": 9, "size": 6, "x": 7, "y": 8}
        s1c = Square.create(**s1)
        s2c = Square.create(**s2)
        self.assertEqual("[Square] (2) 4/0 - 3", str(s1c))
        self.assertEqual("[Square] (9) 7/8 - 6", str(s2c))
        self.assertIsNot(s1, s1c)
        self.assertIsNot(s2, s2c)
        self.assertNotEqual(s1, s1c)
        self.assertNotEqual(s2, s2c)

    def test_load_from_file_no_file(self):
        """Checks use of load_from_file with no file"""
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_empty_file(self):
        """Checks use of load_from_file with empty file"""
        try:
            os.remove("Square.json")
        except:
            pass
        open("Square.json", 'a').close()
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file(self):
        """test normal use of load_from_file"""
        s1 = Square(2, 3, 4, 5)
        s2 = Square(7, 8, 9, 10)
        li = [s1, s2]
        Square.save_to_file(li)
        lo = Square.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        s1c = lo[0]
        s2c = lo[1]
        self.assertTrue(type(s1c) is Square)
        self.assertTrue(type(s2c) is Square)
        self.assertEqual(str(s1), str(s1c))
        self.assertEqual(str(s2), str(s2c))
        self.assertIsNot(s1, s1c)
        self.assertIsNot(s2, s2c)
        self.assertNotEqual(s1, s1c)
        self.assertNotEqual(s2, s2c)
