#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from string_algorithms.tree import Tree, TreeNode
from string_algorithms.lca import LCA
from string_algorithms.node_mixins import LabeledNode


class LabeledTreeNode(LabeledNode, TreeNode):
    pass


class TestLCA(unittest.TestCase):
    def setUp(self):
        self.tree = Tree(node_class=LabeledTreeNode, label=0)
        self.tree.root.add(1).add(2).add(3)
        self.tree.root.add(4).add(5)
        self.tree.root.get(1).add(6).add(7)
        self.tree.root.get(1).get(2).add(8)
        self.tree.root.get(1).get(2).add(9)
        self.lca = LCA(self.tree)

    def test_query(self):
        self.assertEqual(
            self.lca.query(
                self.tree.root.get(1),
                self.tree.root.get(4),
            ),
            self.tree.root,
        )
        self.assertEqual(
            self.lca.query(
                self.tree.root.get(1).get(2).get(8),
                self.tree.root.get(4).get(5),
            ),
            self.tree.root,
        )
        self.assertEqual(
            self.lca.query(
                self.tree.root.get(1).get(2).get(8),
                self.tree.root.get(1).get(6).get(7),
            ),
            self.tree.root.get(1),
        )
        self.assertEqual(
            self.lca.query(
                self.tree.root.get(1).get(2).get(8),
                self.tree.root.get(1).get(2).get(3),
            ),
            self.tree.root.get(1).get(2),
        )
