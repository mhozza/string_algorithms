#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from string_algorithms.suffix_array import naive_suffix_array, suffix_array


class TestNaiveSuffixArray(unittest.TestCase):
    def test_suffix_array(self):
        text = 'ctaataatg'
        self.assertTupleEqual(naive_suffix_array(text), (2, 5, 3, 6, 0, 8, 1, 4, 7))


class TestSuffixArray(unittest.TestCase):
    def test_suffix_array(self):
        text = 'ctaataatg'
        self.assertTupleEqual(suffix_array(text), (2, 5, 3, 6, 0, 8, 1, 4, 7))

    def test_suffix_array2(self):
        text = 'imimmmisismisissiipi'
        self.assertTupleEqual(
            suffix_array(text), (19, 16, 0, 2, 17, 6, 11, 8, 13, 1, 5, 10, 4, 3, 18, 15, 7, 12, 9, 14)
        )

# Todo: ranodm strings, empty string, aaaa, ...
