import unittest

from string_algorithms.utils import argmin


class TestArgMin(unittest.TestCase):
    def test_first(self):
        self.assertEqual(argmin(3, 4, 7, 4), 0)
        self.assertEqual(argmin(3, 4, 7, 3), 0)

    def test_two(self):
        self.assertEqual(argmin(0, 1), 0)
        self.assertEqual(argmin(0, 0), 0)
        self.assertEqual(argmin(1, 0), 1)

    def test_array(self):
        self.assertEqual(argmin([3, 4, 0, 4]), 2)
        self.assertEqual(argmin([3, 0, 7, 3]), 1)

    def test_middle(self):
        self.assertEqual(argmin(3, 4, 0, 4), 2)
        self.assertEqual(argmin(3, 0, 7, 3), 1)

    def test_last(self):
        self.assertEqual(argmin(3, 4, 7, 4, 1), 4)
        self.assertEqual(argmin(3, 4, 7, 3, 1), 4)
