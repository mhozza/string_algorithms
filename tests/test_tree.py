#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from string_algorithms.node_mixins import LabeledNodeMixin
from string_algorithms.tree import dfs, Tree, TreeNode


class LabeledTreeNode(LabeledNodeMixin, TreeNode):
    pass


class TestTreeNode(unittest.TestCase):
    def test_add(self):
        node = TreeNode(0)
        self.assertDictEqual(node.children, {})
        node.add(1)
        self.assertEqual(len(node.children), 1)
        self.assertTrue(1 in node.children)
        self.assertTrue(node.children[1] is not None)

    def test_next(self):
        node = TreeNode(0)
        self.assertIsNone(node.get(1))
        node2 = node.add(1)
        self.assertIsNotNone(node.get(1))
        self.assertDictEqual(node.get(1).children, {})
        self.assertIsNone(node.get(2))
        node2.add(2)
        self.assertIsNotNone(node.get(1).get(2))
        self.assertIsNone(node.get(2))
        self.assertIsNone(node.get(1).get(3))


class TestEulerTour(unittest.TestCase):
    def test_euler_tour_sorted(self):
        path = []
        depths = []

        def action(node, depth):
            path.append(node)
            depths.append(depth)

        tree = Tree(node_class=LabeledTreeNode, label=0)
        tree.root.add(1).add(2).add(3)
        tree.root.add(4).add(5)
        tree.root.get(1).add(6).add(7)
        tree.root.get(1).get(2).add(8)
        tree.root.get(1).get(2).add(9)

        correct_path = [0, 1, 2, 3, 2, 8, 2, 9, 2, 1, 6, 7, 6, 1, 0, 4, 5, 4, 0]
        correct_depth = [0, 1, 2, 3, 2, 3, 2, 3, 2, 1, 2, 3, 2, 1, 0, 1, 2, 1, 0]
        dfs(tree, action, sort=True)
        self.assertListEqual(depths, correct_depth)
        self.assertListEqual([n.label for n in path], correct_path)

    def test_euler_tour(self):
        path = []
        depths = []

        def action(node, depth):
            path.append(node)
            depths.append(depth)

        tree = Tree(node_class=LabeledTreeNode, label=0)
        tree.root.add(1).add(2).add(3)
        tree.root.add(4).add(5)
        tree.root.get(1).add(6).add(7)
        tree.root.get(1).get(2).add(8)
        tree.root.get(1).get(2).add(9)

        correct_path = [0, 1, 2, 3, 2, 8, 2, 9, 2, 1, 6, 7, 6, 1, 0, 4, 5, 4, 0]
        correct_depth = [0, 1, 2, 3, 2, 3, 2, 3, 2, 1, 2, 3, 2, 1, 0, 1, 2, 1, 0]
        dfs(tree, action)
        self.assertListEqual(depths, correct_depth)
        self.assertCountEqual([n.label for n in path], correct_path)
