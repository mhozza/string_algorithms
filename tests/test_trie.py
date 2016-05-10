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
        self.assertIsNone(node.next('a'))
        node2 = node.add('a')
        self.assertIsNotNone(node.next('a'))
        self.assertDictEqual(node.next('a').children, {})
        self.assertIsNone(node.next('b'))
        node2.add('b')
        self.assertIsNotNone(node.next('a').next('b'))
        self.assertIsNone(node.next('b'))
        self.assertIsNone(node.next('a').next('c'))


class TestTrie(unittest.TestCase):
    def test_add(self):
        trie = Trie()
        node = trie.root
        trie.add('abc')
        self.assertIsNotNone(node.next('a').next('b').next('c'))
        self.assertTrue(node.next('a').next('b').next('c').is_word)

    def test_get_node(self):
        trie = Trie()
        node = trie.root
        trie.add('abc')
        self.assertEqual(trie.get_node('abc'), node.next('a').next('b').next('c'))

    def test_get_node2(self):
        trie = Trie()
        node = trie.root
        trie.add('abc')
        trie.add('abcd')
        trie.add('aaa')
        trie.add('a')
        trie.add('badacer')
        self.assertEqual(trie.get_node('abc'), node.next('a').next('b').next('c'))
        self.assertIsNotNone(trie.get_node('abc'))
        self.assertIsNotNone(trie.get_node('abcd'))
        self.assertIsNotNone(trie.get_node('aaa'))
        self.assertIsNotNone(trie.get_node('a'))
        self.assertIsNotNone(trie.get_node('badacer'))
