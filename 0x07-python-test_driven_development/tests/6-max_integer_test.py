#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        module_doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        func_doc = max_integer.__doc__
        self.assertTrue(len(func_doc) > 1)

    def test_empty_list(self):
        """Tests for empty list []"""
        empty_list = []
        self.assertIsNone(max_integer(empty_list))

    def test_no_args(self):
        """Tests for no arguments passed to function"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for only one number in the list"""
        one_element = [1]
        self.assertEqual(max_integer(one_element), 1)

    def test_positive_end(self):
        """Tests for all positive with max at end"""
        e_l = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(e_l), 50)

    def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        m_l = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(m_l), 360)

    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""
        b_l = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(b_l), 200)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        on_l = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(on_l), 200)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        n_l = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n_l), -1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [5, 7, "Osoti", 4, 5, "False"]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()
