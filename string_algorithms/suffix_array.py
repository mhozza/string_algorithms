from operator import itemgetter
from collections import Counter

from string_algorithms.utils import inverse_index


def naive_suffix_array(s):
    return tuple(x[1] for x in sorted((s[i:], i) for i in range(len(s))))


def suffix_array(s):
    """
    Induced sorting implementation of linear time suffix array construction
    :param s:string
    :return: tuple
    """

    # compute type
    t = [1] * len(s)
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i+1]:
            t[i] = 0
        elif s[i] > s[i + 1]:
            t[i] = 1
        else:
            t[i] = t[i+1]

    # compute bucket sizes:
    freq = Counter(s)
    alphabet = tuple(sorted(freq.keys()))
    inverse_alphabet = inverse_index(alphabet)
    buckets = []
    sum = 0
    for a in alphabet:
        buckets.append((sum, sum + freq[a]))
        sum += freq[a]

    # phase 1: sort LMS positions
    # @FIXME: dummy implementation for now
    lms = [i for i in range(1, len(s)) if t[i] == 0 and t[i-1] == 1]
    sorted_lms = tuple(x[1] for x in sorted((s[i:], i) for i in lms))

    a = [None] * len(s)
    # phase 2:
    # (2.1)
    counters = [e for _, e in buckets]
    for p in reversed(sorted_lms):
        a[counters[inverse_alphabet[s[p]]] - 1] = p
        counters[inverse_alphabet[s[p]]] -= 1

    # (2.2)
    counters = [b for b, _ in buckets]
    a[counters[inverse_alphabet[s[-1]]]] = len(s) - 1
    counters[inverse_alphabet[s[-1]]] += 1
    for i in a:
        if i is None or i <= 0:
            continue
        p = i - 1
        if t[p] == 1:
            a[counters[inverse_alphabet[s[p]]]] = p
            counters[inverse_alphabet[s[p]]] += 1

    # (2.3)
    counters = [e for _, e in buckets]
    for i in reversed(a):
        if i is None or i <= 0:
            continue
        p = i - 1
        if t[p] == 0:
            a[counters[inverse_alphabet[s[p]]] - 1] = p
            counters[inverse_alphabet[s[p]]] -= 1

    return tuple(a)
