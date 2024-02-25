#!/usr/bin/python3
"""Module that defines a test class"""
import io
import unittest
import unittest.mock
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test class for Square"""
    def test_square_class_inheritance(self):
        """test if Square inherits from Basee"""
        s = Square(5, 2, 1)
        self.assertIsInstance(s, Square)
        self.assertIsInstance(s, Base)

    def assertSquareAttributes(self, s, size, x, y, id):
        """Helper method to assert square attributes"""
        self.assertEqual(s.size, size)
        self.assertEqual(s.width, size)
        self.assertEqual(s.height, size)
        self.assertEqual(s.x, x)
        self.assertEqual(s.y, y)
        self.assertEqual(s.id, id)

    def test_display_method(self):
        """test if display method prints square with '#' character"""
        s = Square(3, 1, 1)
        expected_output = "###\n ###\n ###"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_str_method(self):
        """test if __str__ method returns the correct string representation"""
        s = Square(4, 2, 1, 12)
        expected_output = "[Square] (12) 2/1 - 4"
        self.assertEqual(str(s), expected_output)

    def test_update_method_args(self):
        """Test if update method assigns values correctly with  *args"""
        s = Square(1, 2, 3, 4)
        s.update(10, 20, 30, 40)
        self.assertSquareAttributes(s, 10, 20, 30, 0)

    def test_update_method_kwargs(self):
        """Test if method assigns values correctly with **kwargs"""
        s = Square(1, 2, 3, 4)
        s.update(id=10, size=20, x=30, y=40)
        self.assertSquareAttributes(s, 10, 30, 40, 10)

    def test_update_method_mixed_args_kwargs(self):
        """test if update method assigns values correctly with mixed
        *args and **kwargs
        """
        s = Square(1, 2, 3, 4)
        s.update(10, size=20, x=30, y=40)
        self.assertSquareAttributes(s, 1, 2, 3, 10)

    def test_square_update(self):
        """test square update method"""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

        s.update(size=10, x=5)
        self.assertEqual(str(s), "[Square] (1) 5/4 - 10")

        s.update(y=7, size=20)
        self.assertEqual(str(s), "[Square] (1) 5/7 - 20")

    def test_square_update_args_kwargs(self):
        """test square update method with args and kwargs"""
        s = Square(5)
        s.update(1, 2, 3, 4, size=10, x=5, y=7)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_square_to_dictionary(self):
        """test square to_dictionary method"""
        s = Square(5, 2, 3, 1)
        expected_dict = {'id': s.id, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(s.to_dictionary(), expected_dict)

    def test_square_to_dictionary_empty(self):
        """Test square to_dictionary method with default values"""
        s = Square(1)
        expected_dict = {'id': s.id, 'size': 1, 'x': 0, 'y': 0}
        self.assertDictEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
