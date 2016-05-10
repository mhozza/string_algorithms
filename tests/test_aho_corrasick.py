#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from string_algorithms.aho_corrasick import find, preprocess
from string_algorithms.naive_find import find as naive_find


class TestAhoCorrasickPreprocess(unittest.TestCase):
    def test_preprocess(self):
        patterns = ('at', 'gag', 'gc', 'gata')
        t, _ = preprocess(patterns)
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

        self.assertSetEqual(result, set(find(patterns, text)))
