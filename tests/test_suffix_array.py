#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string
import unittest

from string_algorithms.suffix_array import naive_suffix_array, suffix_array


class TestNaiveSuffixArray(unittest.TestCase):
    def test_empty_string(self):
        self.assertTupleEqual(
            suffix_array(''), tuple()
        )

    def test_suffix_array(self):
        text = 'ctaataatg'
        self.assertTupleEqual(naive_suffix_array(text), (2, 5, 3, 6, 0, 8, 1, 4, 7))

    def test_suffix_array2(self):
        text = 'imimmmisismisissiipi'
        self.assertTupleEqual(
            suffix_array(text), (19, 16, 0, 2, 17, 6, 11, 8, 13, 1, 5, 10, 4, 3, 18, 15, 7, 12, 9, 14)
        )

class TestSuffixArray(unittest.TestCase):
    def test_empty_string(self):
        self.assertTupleEqual(
            suffix_array(''), tuple()
        )

    def test_suffix_array(self):
        text = 'ctaataatg'
        self.assertTupleEqual(suffix_array(text), (2, 5, 3, 6, 0, 8, 1, 4, 7))

    def test_suffix_array2(self):
        text = 'imimmmisismisissiipi'
        self.assertTupleEqual(
            suffix_array(text), (19, 16, 0, 2, 17, 6, 11, 8, 13, 1, 5, 10, 4, 3, 18, 15, 7, 12, 9, 14)
        )

    def test_random_strings(self):
        alphabet = string.printable
        cnt = 200
        max_length = 1000
        for t in range(cnt):
            length = random.randint(1, max_length)
            text = ''.join(random.choice(alphabet) for _ in range(length))
            self.assertTupleEqual(
                suffix_array(text), naive_suffix_array(text)
            )

    def test_random_aaaa(self):
        lengths = [1, 2, 3, 10, 100, 1000]
        for length in lengths:
            text = ''.join('a' for _ in range(length))
            self.assertTupleEqual(
                suffix_array(text), naive_suffix_array(text)
            )
