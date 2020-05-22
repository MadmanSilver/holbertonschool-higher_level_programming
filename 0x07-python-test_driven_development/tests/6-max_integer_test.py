import unittest
import random
max_int = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_valid(self):
        for step in range(1024):
            arr = []
            tmp = random.randint(-1024, 1024)
            res = tmp
            for i in range(random.randint(1, 50)):
                arr.append(tmp)
                if tmp > res:
                    res = tmp
                tmp = random.randint(-1024, 1024)
            self.assertEqual(max_int(arr), res)

    def test_empty(self):
        self.assertIsNone(max_int([]))

    def test_except(self):
        with self.assertRaises(Exception):
            max_int("ye")
            max_int(123)
            max_int(["ye", "no"])
            max_int([123, "he"])
