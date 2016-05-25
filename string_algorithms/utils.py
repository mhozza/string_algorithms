from operator import itemgetter
from math import log2, floor


def argmin(iterable):
    return min(enumerate(iterable), key=itemgetter(1))


def greatest_pow2(n):
    return 2 ** floor(log2(n))


def inverse_index(s):
    return {v: k for k, v in enumerate(s)}
