#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from string_algorithms.trie import Trie, TrieNode


class TestTrieNode(unittest.TestCase):
    def test_add(self):
        node = TrieNode()
        self.assertDictEqual(node.children, {})
        node.add('a')
        self.assertEqual(len(node.children), 1)
        self.assertTrue('a' in node.children)
        self.assertTrue(node.children['a'] is not None)

    def test_next(self):
        node = TrieNode()
        self.assertIsNone(node.get('a'))
        node2 = node.add('a')
        self.assertIsNotNone(node.get('a'))
        self.assertDictEqual(node.get('a').children, {})
        self.assertIsNone(node.get('b'))
        node2.add('b')
        self.assertIsNotNone(node.get('a').get('b'))
        self.assertIsNone(node.get('b'))
        self.assertIsNone(node.get('a').get('c'))


class TestTrie(unittest.TestCase):
    def test_add(self):
        trie = Trie()
        node = trie.root
        trie.add('abc')
        self.assertIsNotNone(node.get('a').get('b').get('c'))
        self.assertTrue(node.get('a').get('b').get('c').is_word)

    def test_get_node(self):
        trie = Trie()
        node = trie.root
        trie.add('abc')
        self.assertEqual(trie.get_node('abc'), node.get('a').get('b').get('c'))

    def test_get_node2(self):
        trie = Trie()
        node = trie.root
        trie.add('abc')
        trie.add('abcd')
        trie.add('aaa')
        trie.add('a')
        trie.add('badacer')
        self.assertEqual(trie.get_node('abc'), node.get('a').get('b').get('c'))
        self.assertIsNotNone(trie.get_node('abc'))
        self.assertIsNotNone(trie.get_node('abcd'))
        self.assertIsNotNone(trie.get_node('aaa'))
        self.assertIsNotNone(trie.get_node('a'))
        self.assertIsNotNone(trie.get_node('badacer'))
