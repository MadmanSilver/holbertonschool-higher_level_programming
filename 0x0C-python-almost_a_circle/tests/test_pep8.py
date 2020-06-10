#!/usr/bin/python3
""" Tests pep8 validation. """
import unittest
import pep8


class TestCodeFormat(unittest.TestCase):
    """ Tests pep8 validation. """
    def test_pep8_base(self):
        """ Tests pep8 validation for base.py. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)
    def test_pep8_rectangle(self):
        """ Tests pep8 validation for rectangle.py. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)
    def test_pep8_square(self):
        """ Tests pep8 validation for square.py. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0)
