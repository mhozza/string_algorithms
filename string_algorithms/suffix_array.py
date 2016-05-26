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
    if not s:
        return tuple()

    def is_lms(i):
        if i == 0:
            return False
        return t[i] == 0 and t[i-1] == 1

    def is_equal(i, j):
        if s[i] != s[j]:
            return False
        i += 1
        j += 1
        while s[i] == s[j] and not is_lms(i) and not is_lms(j):
            i += 1
            j += 1
        return s[i] == s[j]

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
    a = [None] * len(s)
    lms = [i for i in range(1, len(s)) if is_lms(i)]
    # (1.1)
    counters = [e for _, e in buckets]
    for p in reversed(lms):
        a[counters[inverse_alphabet[s[p]]] - 1] = p
        counters[inverse_alphabet[s[p]]] -= 1

    # (1.2)
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

    # (1.3)
    counters = [e for _, e in buckets]
    for i in reversed(a):
        if i is None or i <= 0:
            continue
        p = i - 1
        if t[p] == 0:
            a[counters[inverse_alphabet[s[p]]] - 1] = p
            counters[inverse_alphabet[s[p]]] -= 1

    # (1.4)
    j = 0
    prev = None
    LN = dict()
    for i in filter(is_lms, a):
        if prev is None:
            LN[i] = j
            prev = i
        else:
            if not is_equal(i, prev):
                j += 1
            LN[i] = j
            prev = i

    # (1.5)
    ss = [LN[i] for i in lms]
    if j == len(s) - 1:
        # (1.6)
        ssa = ss
    else:
        # (1.7)
        ssa = suffix_array(ss)
    # (1.8)
    sorted_lms = [lms[ssa[i]] for i in range(len(lms))]

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
