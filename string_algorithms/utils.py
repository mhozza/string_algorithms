from math import floor, log2
from operator import itemgetter


def argmin(*args):
    if len(args) == 1:
        iterable = args[0]
    else:
        iterable = args
    return min((j, i) for i, j in enumerate(iterable))[1]


def greatest_pow2(n):
    return 2 ** floor(log2(n))


def inverse_index(a):
    return {v: k for k, v in enumerate(a)}


def inverse_index_array(a):
    ia = [None] * len(a)
    for i, v in enumerate(a):
        ia[v] = i
    return ia
