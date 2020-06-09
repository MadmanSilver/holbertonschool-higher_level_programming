#!/usr/bin/python3
""" Tests the Rectangle class. """
import unittest
import random
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests the Rectangle class. """
    def test_init(self):
        """ Tests rectanlge creation. """
        rec = Rectangle(1, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 1)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        rec = Rectangle(1, 1, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 1)
        self.assertEqual(rec.x, 1)
        self.assertEqual(rec.y, 0)
        rec = Rectangle(1, 1, 1, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 1)
        self.assertEqual(rec.x, 1)
        self.assertEqual(rec.y, 1)
        rec = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 1)
        self.assertEqual(rec.x, 1)
        self.assertEqual(rec.y, 1)
        self.assertEqual(rec.id, 1)

    def test_width(self):
        """ Tests the width attribute. """
        rec = Rectangle(1, 1)
        self.assertEqual(rec.width, 1)
        for i in range(1, 100):
            rec.width = i
            self.assertEqual(rec.width, i)
        with self.assertRaises(TypeError):
            rec.width = None
        with self.assertRaises(ValueError):
            rec.width = 0
        with self.assertRaises(ValueError):
            rec.width = -1
        with self.assertRaises(TypeError):
            rec.width = 1.0
        with self.assertRaises(TypeError):
            rec.width = ""
        with self.assertRaises(TypeError):
            rec.width = []
        with self.assertRaises(TypeError):
            rec.width = {}
        with self.assertRaises(TypeError):
            rec.width = ()

    def test_height(self):
        """ Tests the height attribute. """
        rec = Rectangle(1, 1)
        self.assertEqual(rec.height, 1)
        for i in range(1, 100):
            rec.height = i
            self.assertEqual(rec.height, i)
        with self.assertRaises(TypeError):
            rec.height = None
        with self.assertRaises(ValueError):
            rec.height = 0
        with self.assertRaises(ValueError):
            rec.height = -1
        with self.assertRaises(TypeError):
            rec.height = 1.0
        with self.assertRaises(TypeError):
            rec.height = ""
        with self.assertRaises(TypeError):
            rec.height = []
        with self.assertRaises(TypeError):
            rec.height = {}
        with self.assertRaises(TypeError):
            rec.height = ()

    def test_x(self):
        """ Tests the x attribute. """
        rec = Rectangle(1, 1)
        self.assertEqual(rec.x, 0)
        for i in range(0, 100):
            rec.x = i
            self.assertEqual(rec.x, i)
        with self.assertRaises(TypeError):
            rec.x = None
        with self.assertRaises(ValueError):
            rec.x = -1
        with self.assertRaises(TypeError):
            rec.x = 1.0
        with self.assertRaises(TypeError):
            rec.x = ""
        with self.assertRaises(TypeError):
            rec.x = []
        with self.assertRaises(TypeError):
            rec.x = {}
        with self.assertRaises(TypeError):
            rec.x = ()

    def test_y(self):
        """ Tests the y attribute. """
        rec = Rectangle(1, 1)
        self.assertEqual(rec.y, 0)
        for i in range(0, 100):
            rec.y = i
            self.assertEqual(rec.y, i)
        with self.assertRaises(TypeError):
            rec.y = None
        with self.assertRaises(ValueError):
            rec.y = -1
        with self.assertRaises(TypeError):
            rec.y = 1.0
        with self.assertRaises(TypeError):
            rec.y = ""
        with self.assertRaises(TypeError):
            rec.y = []
        with self.assertRaises(TypeError):
            rec.y = {}
        with self.assertRaises(TypeError):
            rec.y = ()

    def test_area(self):
        """ Tests the area instance method. """
        rec = Rectangle(10, 10)
        self.assertEqual(rec.area(), 100)
        for i in range(1, 100):
            rec.width = i
            self.assertEqual(rec.area(), 10 * i)

    def test_str(self):
        """ Tests the __str__ instance method. """
        rec = Rectangle(10, 10)
        self.assertEqual(str(rec), "[Rectangle] ({}) 0/0 - 10/10\
".format(rec.id))
        for i in range(1, 100):
            rec.width = i
            self.assertEqual(str(rec), "[Rectangle] ({}) 0/0 - {}/10\
".format(rec.id, rec.width))

    def test_update(self):
        """ Tests the update instance method. """
        rec = Rectangle(1, 1)
        for i in range(1, 100):
            args = []
            for j in range(random.randrange(0, 5)):
                args.append(random.randrange(1, 100))
            rec.update(*args)
            l = len(args)
            if l > 0:
                self.assertEqual(rec.id, args[0])
            if l > 1:
                self.assertEqual(rec.width, args[1])
            if l > 2:
                self.assertEqual(rec.height, args[2])
            if l > 3:
                self.assertEqual(rec.x, args[3])
            if l > 4:
                self.assertEqual(rec.y, args[4])

        kwargs = {"id": 10, "width": 11, "height": 12, "x": 13, "y": 14}
        rec.update(**kwargs)
        self.assertEqual(rec.id, 10)
        self.assertEqual(rec.width, 11)
        self.assertEqual(rec.height, 12)
        self.assertEqual(rec.x, 13)
        self.assertEqual(rec.y, 14)

    def test_to_dict(self):
        """ Tests the t0_dictionary instance method. """
        rec = Rectangle(1, 1)
        self.assertEqual(rec.to_dictionary(), {'id': rec.id, 'width': 1, '\
height': 1, 'x': 0, 'y': 0})
