#!/usr/bin/python3
"""This is a unittest for class Base"""


import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Class to define the testCases"""
    def test_base_class_instantiation(self):
        """Testing for base instantiation"""
        b = Base()
        self.assertIsInstance(b, Base)

    def test_to_json_string_empty(self):
        """Test Base to_json_string method with an empty list"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string(self):
        """Test Base to_json_string method with a list of dictionaries"""
        list_of_dicts = [{'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 3},
                {'id': 2, 'width': 7, 'height': 7, 'x': 0, 'y': 0}]
        expected_json = """[{"id": 1, "width": 10, "height": 5, "x": 2, "y": 3}, {"id": 2, "width": 7, "height": 7, "x": 0, "y": 0}]"""
        json_string = Base.to_json_string(list_of_dicts)
        self.assertEqual(json_string, expected_json)

    def test_to_json_string_none(self):
        """test base to_json_string method with None as argument"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string(self):
        """test to_json_string method
        r = Rectangle(10, 7, 2, 8)
        dictionary = r.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(json_string, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')
        """
        b1 = Base(1)
        json_string = Base.to_json_string([b1.to_dictionary()])
        expected_json = '[{"id": 1}]'
        self.assertEqual(json_string, expected_json)

    def test_save_to_file(self):
        """Test save_to_file method
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        filename = "Rectangle.json"

        try:
            os.remove(filename)
        except OSError:
            pass
        """
        b1 = Base(1)
        b2 = Base(2)

        Base.save_to_file([b1, b2])

        with open("Base.json", 'r') as f:
            content = f.read()
        expected_content = '[{"id": 1, {"id": 2}]'
        self.assertEqual(content, expected_content) #'[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]')

        # os.remove(filename)

    def test_from_json_string(self):
        """Test Base class static method from_json_string"""
        # self.assertEqual(Base.from_json_string(None), [])

        # self.assertEqual(Base.from_json_string(""), [])

        json_string = '[{"id": 1}, {"id": 2}]' # '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        expected_list = [{"id": 1}, {"id": 2}] # [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]
        self.assertCountEqual(Base.from_json_string(json_string), expected_list)

    def test_base_instance(self):
        """test creating a Base instance"""
        b = Base()
        self.assertEqual(b.id, 1)

    def tes_base_instance_with_id(self):
        """Test creating a Base instance with specified id"""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_base_instance_with_negative_id(self):
        """Test creating a Base instance with negative id"""
        b = Base(5)
        self.assertEqual(b.id, -5)

    def test_to_json_string(self):
        """Test to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        json_string = Base.to_json_string(list_dicts)
        expected_json = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        self.assertEqual(json_string, expected_json)

    def test_to_json_string_empty(self):
        """Test to_json_string method with empty list"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test to_json_string method with None"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_save_to_file(self):
        """Test save to file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        filename = "Rectangle.json"
        list_objs = [r1, r2]
        Base.save_to_file(list_objs)
        with open(filename, 'r') as f:
            content = f.read()
        expected_json = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        self.assertEqual(content, expected_json)

    def test_save_to_file_empty(self):
        """Test save_to_file method with empty list"""
        filename = "Rectangle.json"
        list_objs = []
        Base.save_to_file(list_objs)
        with open(filename, 'r') as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_none(self):
        """test save_to_file method with none"""
        filename = "Rectangle.json"
        Base.save_to_file(None)
        with open(filename, 'r') as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_from_json_string(self):
        """Test from_json_string method"""
        json_string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        list_objs = Base.from_json_string(json_string)
        expected_list = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]
        self.assertEqual(list_objs, expected_list)

    def test_from_json_string_empty(self):
        """test from_json_string method with empty string"""
        list_objs = Base.from_json_string("")
        self.assertEqual(list_objs, [])

    def test_from_json_string_none(self):
        """test from_json_string method with none"""
        list_objs = Base.from_json_string(None)
        self.assertEqual(list_objs, [])

    def test_create(self):
        """test create method"""
        r_dict = {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 8)

    def test_load_from_file(self):
        """test load_from_file method"""
        filename = "Rectangle.json"
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_objs = [r1, r2]
        Base.save_to_file(list_objs)
        loaded_objs = Base.load_from_file()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1], 2)

    def test_load_from_file_empty(self):
        """Test load_from_file method with empty file"""
        filename = "Rectangle.json"
        list_objs = Base.load_from_file()
        self.assertEqual(list_objs, [])

    def test_load_from_file_nonexistent(self):
        """Test load_from_file method with nonexistent file"""
        filename = "Nonexistent.json"
        list_objs = Base.load_from_file()
        self.assertEqual(list_objs, [])

    def tearDown(self):
        """Clean up after each test case"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
