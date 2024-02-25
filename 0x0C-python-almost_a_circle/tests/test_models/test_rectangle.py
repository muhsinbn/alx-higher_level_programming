#!/usr/bin/python3
"""Module to test for Rectangle class"""

import io
import unittest.mock
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """test class"""
    def test_rectangle_class_inheritance(self):
        """Tests for initialization of the Rectangle class
        """
        r = Rectangle(10, 20)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Base)

    def assertRectangleAttributes(self, r, width, height, x, y, id):
        """helper method to assert Rectangle attributes"""
        self.assertEqual(r.width, width)
        self.assertEqual(r.height, height)
        self.assertEqual(r.x, x)
        self.assertEqual(r.id, id)

    def test_single_argument(self):
        """Test Rectangle initialization with single argument"""
        with self.assertRaises(TypeError):
            r = Rectangle(10)

    def test_two_arguments(self):
        """Test Rectangle with two arguments"""
        r = Rectangle(10, 20)
        self.assertRectangleAttributes(r, 10, 20, 0, 0, 6)

    def test_three_arguments(self):
        """Test Rectangle with three arguments"""
        r = Rectangle(10, 20, 30)
        self.assertRectangleAttributes(r, 10, 20, 30, 0, 5)

    def test_four_arguments(self):
        """Test Rectangle with four arguments"""
        r = Rectangle(10, 20, 30, 40)
        self.assertRectangleAttributes(r, 10, 20, 30, 40, 3)

    def test_all_arguments(self):
        """Test Rectangle with all arguments"""
        r = Rectangle(10, 20, 30, 40, 1)
        self.assertRectangleAttributes(r, 10, 20, 30, 40, 1)

    def test_invalid_width(self):
        """Test handling invalid width"""
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 20)

    def test_invalid_height(self):
        """test handling invalid height"""
        with self.assertRaises(ValueError):
            r = Rectangle(10, -20)

    def test_invalid_x(self):
        """Test handling invalid x"""
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -30)

    def test_invalid_y(self):
        """Test handling invalid y"""
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 30, -40)

    def test_invalid_type(self):
        """Test handling invalid type"""
        with self.assertRaises(TypeError):
            r = Rectangle("not_an_integer")

    def test_area_method(self):
        """Test if the area method exists and returns the correct value"""
        r = Rectangle(10, 20)
        self.assertTrue(hasattr(r, 'area'))
        self.assertEqual(r.area(), 200)

    def test_display_method(self):
        """Test if display method prints rectangle with '#' character"""
        r = Rectangle(3, 2, 1, 1)
        expected_output = "###\n ###"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO
                ) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_str_method(self):
        """Test if __str__ method returns the correct string representation"""
        r = Rectangle(4, 6, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r), expected_output)

    def test_update_method_args(self):
        """test if the update method assigns values correctly"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40, 50)
        self.assertRectangleAttributes(r, 20, 30, 40, 50, 10)

    def test_update_method_kwargs(self):
        """test if method assigns values correctly with **kwargs"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=0, width=20, height=30, x=40, y=50)
        self.assertRectangleAttributes(r, 20, 30, 40, 50, 0)

    def test_update_method_mixed_args_kwargs(self):
        """Test if update method assigns value correctly with *args
        and **kwargs
        """
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, width=20, height=30, x=40, y=50)
        self.assertRectangleAttributes(r, 1, 2, 3, 4, 10)

    def test_rectangle_to_dictionary(self):
        """test Rectangle to dictionary method"""
        r = Rectangle(10, 5, 2, 3, 1)
        expected_dict = {'id': r.id, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_rectangle_to_dictionary_empty(self):
        """Test Rectangle to_dictionary method with default value"""
        r = Rectangle(1, 1)
        expected_dict = {'id': r.id, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        self.assertEqual(r.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()
