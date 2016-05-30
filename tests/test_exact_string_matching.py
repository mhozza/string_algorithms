#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from string_algorithms.exact_string_matching import (aho_corrasick,
                                                     aho_corrasick_preprocess,
                                                     kmp, kmp_preprocess,
                                                     naive_find,
                                                     suffix_array_match, sa_preprocess)
from string_algorithms.suffix_array import suffix_array, lcp_array, LCPConceptualIntervalTree


class TestNaiveFind(unittest.TestCase):
    def test_not_find(self):
        text = 'tatatattgcgccatattagagattagatagga'
        self.assertListEqual(naive_find('alt', text), [])

    def test_find(self):
        text = 'tatatattgcgccatattagagattagatagga'
        self.assertListEqual(naive_find('at', text), [1, 3, 5, 13, 15, 22, 27])
        self.assertListEqual(naive_find('gag', text), [19])
        self.assertListEqual(naive_find('gc', text), [8, 10])
        self.assertListEqual(naive_find('gata', text), [26])


class TestKMPPreprocess(unittest.TestCase):
    def test_empty(self):
        pattern = ''
        p = kmp_preprocess(pattern)
        self.assertEqual(len(p), 0)

    def test_tiny(self):
        pattern = 'a'
        p = kmp_preprocess(pattern)
        self.assertEqual(len(p), 1)
        self.assertListEqual(p, [0])

    def test_small(self):
        pattern = 'at'
        p = kmp_preprocess(pattern)
        self.assertEqual(len(p), 2)
        self.assertListEqual(p, [0, 0])

    def test_small2(self):
        pattern = 'aa'
        p = kmp_preprocess(pattern)
        self.assertEqual(len(p), 2)
        self.assertListEqual(p, [0, 1])

    def test_repetitive(self):
        pattern = 'tatata'
        p = kmp_preprocess(pattern)
        self.assertEqual(len(p), len(pattern))
        self.assertListEqual(p, [0, 0, 1, 2, 3, 4])

    def test_repetitive2(self):
        pattern = 'aaaaaa'
        p = kmp_preprocess(pattern)
        self.assertEqual(len(p), len(pattern))
        self.assertListEqual(p, [0, 1, 2, 3, 4, 5])

    def test_almost_repetitive(self):
        pattern = 'ananas'
        p = kmp_preprocess(pattern)
        self.assertEqual(len(p), len(pattern))
        self.assertListEqual(p, [0, 0, 1, 2, 3, 0])

    def test_nonrepetitive(self):
        pattern = 'abcdefgh'
        p = kmp_preprocess(pattern)
        self.assertEqual(len(p), len(pattern))
        self.assertListEqual(p, [0] * len(pattern))


class TestKMP(unittest.TestCase):
    def test_not_find(self):
        text = 'tatatattgcgccatattagagattagatagga'
        self.assertListEqual(kmp('alt', text), [])

    def test_small(self):
        patterns = ('at', 'gag', 'gc', 'gata')
        text = 'tatatattgcgccatattagagattagatagga'
        for pattern in patterns:
            self.assertListEqual(kmp(pattern, text), naive_find(pattern, text))


class TestAhoCorrasickPreprocess(unittest.TestCase):
    def test_preprocess(self):
        patterns = ('at', 'gag', 'gc', 'gata')
        t, _ = aho_corrasick_preprocess(patterns)
        self.assertEqual(t.get_node('ga').fail, t.get_node('a'))
        self.assertEqual(t.get_node('gag').fail, t.get_node('g'))
        self.assertEqual(t.get_node('gat').fail, t.get_node('at'))
        self.assertEqual(t.get_node('gata').fail, t.get_node('a'))
        self.assertEqual(t.get_node('at').fail, t.root)
        self.assertEqual(t.get_node('a').fail, t.root)


class TestAhoCorrasick(unittest.TestCase):
    def test_find(self):
        patterns = ('at', 'gag', 'gc', 'gata')
        text = 'tatatattgcgccatattagagattagatagga'
        result = set()
        for pattern in patterns:
            occurrences = naive_find(pattern, text)
            result |= set(((o, pattern) for o in occurrences))

        self.assertSetEqual(result, set(aho_corrasick(patterns, text)))


class TestSAMatch(unittest.TestCase):
    def test_not_find(self):
        text = 'tatatattgcgccatattagagattagatagga'
        t = sa_preprocess(text)
        self.assertListEqual(suffix_array_match('alt', t), [])

    def test_small(self):
        patterns = ('at', 'gag', 'gc', 'gata')
        text = 'tatatattgcgccatattagagattagatagga'
        t = sa_preprocess(text)
        for pattern in patterns:
            self.assertListEqual(suffix_array_match(pattern, t, sort=True), naive_find(pattern, text))

    def test_small2(self):
        text = 'ctaataatg'
        t = sa_preprocess(text)
        self.assertListEqual(suffix_array_match('taa', t, sort=True), naive_find('taa', text))
