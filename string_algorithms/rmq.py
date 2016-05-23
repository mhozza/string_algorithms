from math import ceil, floor, log2

from .utils import argmin, greatest_pow2


class RMQ:
    def __init__(self, array):
        self.array = array
        self.block_size = ceil(log2(len(array)) / 4)
        self.block_cnt = ceil(len(self.array) / self.block_size)
        self.block_mins = self._calculate_block_mins()
        self.processed_block_mins = self._process_block_mins()

    def _block_element(self, block, index):
        i = self.block_size * block + index
        if 0 <= i < len(self.array):
            return self.array[i]
        raise IndexError()

    def _max_element_index(self, block):
        return min(self.block_size, len(self.array) - self.block_size * block)

    def _block_items(self, block, start=0, end=None):
        if end is None:
            end = self._max_element_index(block)
        return (
            self._block_element(block, i) for i in range(start, end)
        )

    def _get_block(self, i):
        return i // self.block_size, i % self.block_size

    def _calculate_block_mins(self):
        return [
            argmin(self._block_items(b))
            for b in range(self.block_cnt)
        ]

    def _process_block_mins(self):
        max_size = floor(log2(len(self.block_mins)))
        res = [[i for _, i in self.block_mins]]
        for si in range(max_size):
            t = [
                min(res[si][i], res[si][i + 2**si]) for i in range(len(self.block_mins) - 2**si)
            ] + [
                res[si][i] for i in range(len(self.block_mins) - 2**si, len(self.block_mins))
            ]
            res.append(t)

        return res

    def _query_whole_blocks(self, bi, bj):
        cnt = floor(log2(bj - bi))
        print(bi, bj, bj - 2**cnt, cnt, self.block_cnt)
        return min(
            self.processed_block_mins[cnt][bi],
            self.processed_block_mins[cnt][bj - 2**cnt],
        )

    def _query_partial_block(self, b, i=0, j=None):
        if j is None:
            j = self._max_element_index(b)
        # @TODO: replace with fast precomputed version
        return min(self._block_items(b, i, j))

    def query(self, i, j):
        bi, pi = self._get_block(i)
        bj, pj = self._get_block(j)
        m = None
        if bi == bj:
            return self._query_partial_block(bi, i=pi, j=pj)
        if pi:
            m = self._query_partial_block(bi, i=pi)
            bi += 1
        if pj:
            mj = self._query_partial_block(bj, j=pj)
            if m is None or mj < m:
                m = mj
        if bi < bj:
            print(i, j, bi, bj)
            mb = self._query_whole_blocks(bi, bj)
            if m is None or mb < m:
                m = mb
        return m
