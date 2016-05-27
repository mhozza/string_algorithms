#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string
import unittest

from string_algorithms.suffix_array import naive_suffix_array, suffix_array, lcp_array


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


class TestLCPArray(unittest.TestCase):
    def test_empty_string(self):
        self.assertTupleEqual(
            suffix_array(''), tuple()
        )

    def test_lcp_array(self):
        text = 'ctaataatg'
        sa = suffix_array(text)
        self.assertTupleEqual(lcp_array(text, sa), (0, 3, 1, 2, 0, 0, 0, 4, 1))

    def test_random_strings(self):
        alphabet = string.printable
        cnt = 200
        max_length = 1000
        for t in range(cnt):
            length = random.randint(1, max_length)
            text = ''.join(random.choice(alphabet) for _ in range(length))
            sa = suffix_array(text)
            lcpa = lcp_array(text, sa)
            for i in range(1, len(lcpa)):
                self.assertEqual(
                    text[sa[i]:sa[i] + lcpa[i]],
                    text[sa[i-1]:sa[i-1] + lcpa[i]],
                )
                if sa[i] + lcpa[i] + 1 < len(text) and sa[i - 1] + lcpa[i] + 1 < len(text):
                    self.assertNotEqual(
                        text[sa[i]:sa[i] + lcpa[i] + 1],
                        text[sa[i - 1]:sa[i - 1] + lcpa[i] + 1],
                    )

    def test_random_aaaa(self):
        lengths = [1, 2, 3, 10, 100, 1000]
        for length in lengths:
            text = ''.join('a' for _ in range(length))
            sa = suffix_array(text)
            correct_lcp = tuple(i for i in range(len(text)))
            self.assertTupleEqual(
                lcp_array(text, sa), correct_lcp
            )
