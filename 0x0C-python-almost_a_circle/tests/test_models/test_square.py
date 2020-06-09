#!/usr/bin/python3
""" Tests the Square class. """
import unittest
import random
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Tests the Square class. """
    def test_init(self):
        """ Tests rectanlge creation. """
        rec = Square(1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 1)
        self.assertEqual(rec.size, 1)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        rec = Square(1, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 1)
        self.assertEqual(rec.size, 1)
        self.assertEqual(rec.x, 1)
        self.assertEqual(rec.y, 0)
        rec = Square(1, 1, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 1)
        self.assertEqual(rec.size, 1)
        self.assertEqual(rec.x, 1)
        self.assertEqual(rec.y, 1)
        rec = Square(1, 1, 1, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 1)
        self.assertEqual(rec.size, 1)
        self.assertEqual(rec.x, 1)
        self.assertEqual(rec.y, 1)
        self.assertEqual(rec.id, 1)

    def test_size(self):
        """ Tests the size attribute. """
        rec = Square(1)
        self.assertEqual(rec.size, 1)
        for i in range(1, 100):
            rec.size = i
            self.assertEqual(rec.size, i)
            self.assertEqual(rec.width, i)
            self.assertEqual(rec.height, i)
        with self.assertRaises(TypeError):
            rec.size = None
        with self.assertRaises(ValueError):
            rec.size = 0
        with self.assertRaises(ValueError):
            rec.size = -1
        with self.assertRaises(TypeError):
            rec.size = 1.0
        with self.assertRaises(TypeError):
            rec.size = ""
        with self.assertRaises(TypeError):
            rec.size = []
        with self.assertRaises(TypeError):
            rec.size = {}
        with self.assertRaises(TypeError):
            rec.size = ()

    def test_str(self):
        """ Tests the __str__ instance method. """
        rec = Square(10)
        self.assertEqual(str(rec), "[Square] ({}) 0/0 - 10\
".format(rec.id))
        for i in range(1, 100):
            rec.size = i
            self.assertEqual(str(rec), "[Square] ({}) 0/0 - {}\
".format(rec.id, rec.size))

    def test_update(self):
        """ Tests the update instance method. """
        rec = Square(1)
        for i in range(1, 100):
            args = []
            for j in range(random.randrange(0, 4)):
                args.append(random.randrange(1, 100))
            rec.update(*args)
            l = len(args)
            if l > 0:
                self.assertEqual(rec.id, args[0])
            if l > 1:
                self.assertEqual(rec.size, args[1])
            if l > 2:
                self.assertEqual(rec.x, args[2])
            if l > 3:
                self.assertEqual(rec.y, args[3])

        kwargs = {"id": 10, "size": 11, "x": 13, "y": 14}
        rec.update(**kwargs)
        self.assertEqual(rec.id, 10)
        self.assertEqual(rec.size, 11)
        self.assertEqual(rec.x, 13)
        self.assertEqual(rec.y, 14)

    def test_to_dict(self):
        """ Tests the t0_dictionary instance method. """
        rec = Square(1)
        self.assertEqual(rec.to_dictionary(), {'id': rec.id, 'size': 1, '\
x': 0, 'y': 0})
