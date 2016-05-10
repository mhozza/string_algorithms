#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from string_algorithms.kmp import find, preprocess
from string_algorithms.naive_find import find as naive_find


class TestKMPPreprocess(unittest.TestCase):
    def test_empty(self):
        pattern = ''
        p = preprocess(pattern)
        self.assertEqual(len(p), 0)

    def test_tiny(self):
        pattern = 'a'
        p = preprocess(pattern)
        self.assertEqual(len(p), 1)
        self.assertListEqual(p, [0])

    def test_small(self):
        pattern = 'at'
        p = preprocess(pattern)
        self.assertEqual(len(p), 2)
        self.assertListEqual(p, [0, 0])

    def test_small2(self):
        pattern = 'aa'
        p = preprocess(pattern)
        self.assertEqual(len(p), 2)
        self.assertListEqual(p, [0, 1])

    def test_repetitive(self):
        pattern = 'tatata'
        p = preprocess(pattern)
        self.assertEqual(len(p), len(pattern))
        self.assertListEqual(p, [0, 0, 1, 2, 3, 4])

    def test_repetitive2(self):
        pattern = 'aaaaaa'
        p = preprocess(pattern)
        self.assertEqual(len(p), len(pattern))
        self.assertListEqual(p, [0, 1, 2, 3, 4, 5])

    def test_almost_repetitive(self):
        pattern = 'ananas'
        p = preprocess(pattern)
        self.assertEqual(len(p), len(pattern))
        self.assertListEqual(p, [0, 0, 1, 2, 3, 0])

    def test_nonrepetitive(self):
        pattern = 'abcdefgh'
        p = preprocess(pattern)
        self.assertEqual(len(p), len(pattern))
        self.assertListEqual(p, [0] * len(pattern))


class TestKMP(unittest.TestCase):
    def test_small(self):
        patterns = ('at', 'gag', 'gc', 'gata')
        text = 'tatatattgcgccatattagagattagatagga'
        for pattern in patterns:
            self.assertListEqual(find(pattern, text), naive_find(pattern, text))
