#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from random import randint

from string_algorithms.rmq import RMQ


class TestRMQ(unittest.TestCase):
    def setUp(self):
        n = 1001
        self.array = [randint(0, n) for _ in range(n)]
        self.rmq = RMQ(self.array)

    def test_block_items(self):
        self.assertListEqual(
            list(self.rmq._block_items(0)), list(self.array[:self.rmq.block_size])
        )
        self.assertListEqual(
            list(self.rmq._block_items(1)),
            list(self.array[self.rmq.block_size:self.rmq.block_size*2]),
        )
        lb = self.rmq.block_cnt - 1
        pos = lb*self.rmq.block_size
        self.assertListEqual(
            list(self.rmq._block_items(lb)), list(self.array[pos:])
        )

    def test_get_block(self):
        self.assertEqual(self.rmq._get_block(0), (0, 0))
        self.assertEqual(self.rmq._get_block(self.rmq.block_size), (1, 0))
        self.assertEqual(self.rmq._get_block(self.rmq.block_size+1), (1, 1))

    def test_process_block_mins(self):
        for si in range(len(self.rmq.processed_block_mins)):
            for i in range(len(self.rmq.processed_block_mins[si])):
                self.assertEqual(
                    self.rmq.processed_block_mins[si][i],
                    min(i for _, i in self.rmq.block_mins[i:min(i+2**si, len(self.rmq.block_mins))]),
                )

    def test_query_aligned(self):
        test_cnt = 1000
        for t in range(test_cnt):
            b = randint(1, 5)
            i = randint(0, self.rmq.block_cnt - b -1) * self.rmq.block_size
            j = i + b * self.rmq.block_size
            self.assertEqual(self.rmq.query(i, j), min(self.array[i:j]))

    def test_query(self):
        test_cnt = 1000
        for t in range(test_cnt):
            i = randint(0, len(self.array) - 2)
            j = randint(i + 1, len(self.array) - 1)
            self.assertEqual(self.rmq.query(i, j), min(self.array[i:j]))
