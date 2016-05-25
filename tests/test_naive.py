#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from string_algorithms.naive_find import find


class TestNaiveFind(unittest.TestCase):
    def test_find(self):
        text = 'tatatattgcgccatattagagattagatagga'
        self.assertListEqual(find('at', text), [1, 3, 5, 13, 15, 22, 27])
        self.assertListEqual(find('gag', text), [19])
        self.assertListEqual(find('gc', text), [8, 10])
        self.assertListEqual(find('gata', text), [26])
