#!/usr/bin/python3
""" Contains the unittests for the Base class. """
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """ Tests the base class. """
    def test_init(self):
        """ Tests the creation of a base class. """
        base = Base()
        self.assertEqual(base.id, 3)
        base = Base(None)
        self.assertEqual(base.id, 4)
        base = Base()
        self.assertEqual(base.id, 5)
        base = Base(4)
        self.assertEqual(base.id, 4)
        base = Base(7)
        self.assertEqual(base.id, 7)
        base = Base(-1)
        self.assertEqual(base.id, -1)

    def test_to_json(self):
        """ Tests the to_json_string static method. """
        self.assertEqual(Base.to_json_string([{}, {}]), "[{}, {}]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(Base.to_json_string([{"yes": 1}]), "[{\"yes\": 1}]")
        self.assertEqual(Base.to_json_string([{"yes": 1, "no": 0}]), "\
[{\"yes\": 1, \"no\": 0}]")
        self.assertEqual(Base.to_json_string([{"yes": 1}, {"ye": 1}]), "\
[{\"yes\": 1}, {\"ye\": 1}]")
        self.assertEqual(Base.to_json_string([{"yes": 1, "no": 0}, {"ye\
": 1, "nah": 0}]), "[{\"yes\": 1, \"no\": 0}, {\"ye\": 1, \"nah\": 0}]")

    def test_save_to_file(self):
        """ Tests the save_to_file class method. """
        l = []
        Base.save_to_file(l)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), Base.to_json_string(l))
        l = [Rectangle(1, 1), Rectangle(1, 1)]
        Base.save_to_file(l)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(),
                             Base.to_json_string([l[0].to_dictionary(),
                                                  l[1].to_dictionary()]))
        l = [Rectangle(1, 1)]
        Base.save_to_file(l)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(),
                             Base.to_json_string([l[0].to_dictionary()]))
        l = None
        Base.save_to_file(l)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), Base.to_json_string(l))

    def test_from_json(self):
        """ Tests the from_json_string static method. """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string("[{}]"), [{}])
        self.assertEqual(Base.from_json_string("[{}, {}]"), [{}, {}])

    def test_create(self):
        """ Tests the create class method. """
        dict_r = {"width": 10, "height": 10, "id": 10, "x": 10, "y": 10}
        dict_s = {"size": 10, "id": 10, "x": 10, "y": 10}
        obj_r = Rectangle.create(**dict_r)
        obj_s = Square.create(**dict_s)

        self.assertEqual(obj_r.width, dict_r['width'])
        self.assertEqual(obj_r.height, dict_r['height'])
        self.assertEqual(obj_r.id, dict_r['id'])
        self.assertEqual(obj_r.x, dict_r['x'])
        self.assertEqual(obj_r.y, dict_r['y'])
        self.assertEqual(obj_s.width, dict_s['size'])
        self.assertEqual(obj_s.height, dict_s['size'])
        self.assertEqual(obj_s.size, dict_s['size'])
        self.assertEqual(obj_s.id, dict_s['id'])
        self.assertEqual(obj_s.x, dict_s['x'])
        self.assertEqual(obj_s.y, dict_s['y'])

    def test_load_file(self):
        """ Tests the load_from_file class method. """
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

        l = [Rectangle(10, 10), Rectangle(10, 10, 10, 10, 10)]
        Rectangle.save_to_file(l)
        n = Rectangle.load_from_file()
        self.assertTrue(type(n) is list)
        self.assertEqual(n[0].width, l[0].width)
        self.assertEqual(n[0].height, l[0].height)
        self.assertEqual(n[0].x, l[0].x)
        self.assertEqual(n[0].y, l[0].y)
        self.assertEqual(n[1].width, l[1].width)
        self.assertEqual(n[1].height, l[1].height)
        self.assertEqual(n[1].id, l[1].id)
        self.assertEqual(n[1].x, l[1].x)
        self.assertEqual(n[1].y, l[1].y)
