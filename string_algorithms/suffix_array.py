from collections import Counter

from string_algorithms.tree import SimpleTreeNode
from string_algorithms.utils import inverse_index, inverse_index_array


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

    # compute type
    t = [1] * len(s)
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            t[i] = 0
        elif s[i] > s[i + 1]:
            t[i] = 1
        else:
            t[i] = t[i + 1]

    # compute bucket sizes:
    freq = Counter(s)
    alphabet = tuple(sorted(freq.keys()))
    inverse_alphabet = inverse_index(alphabet)
    buckets = []
    sum = 0
    for sa in alphabet:
        buckets.append((sum, sum + freq[sa]))
        sum += freq[sa]

    def is_lms(i):
        if i == 0:
            return False
        return t[i] == 0 and t[i-1] == 1

    def is_equal(i, j):
        if s[i] != s[j]:
            return False
        i += 1
        j += 1
        while i < len(s) - 1 and j < len(s) - 1 and s[i] == s[j] and not is_lms(i) and not is_lms(j):
            i += 1
            j += 1
        return s[i] == s[j]

    def place_lms(lms, a):
        counters = [e for _, e in buckets]
        for p in reversed(lms):
            a[counters[inverse_alphabet[s[p]]] - 1] = p
            counters[inverse_alphabet[s[p]]] -= 1

    def place_l_positions(a):
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

    def place_s_positions(a):
        counters = [e for _, e in buckets]
        for i in reversed(a):
            if i is None or i <= 0:
                continue
            p = i - 1
            if t[p] == 0:
                a[counters[inverse_alphabet[s[p]]] - 1] = p
                counters[inverse_alphabet[s[p]]] -= 1

    # phase 1: sort LMS positions
    sa = [None] * len(s)
    lms = [i for i in range(1, len(s)) if is_lms(i)]
    # (1.1 - 1.3)
    place_lms(lms, sa)
    place_l_positions(sa)
    place_s_positions(sa)
    # (1.4)
    j = 0
    prev = None
    ln = dict()
    for i in filter(is_lms, sa):
        if prev is None:
            ln[i] = j
            prev = i
        else:
            if not is_equal(i, prev):
                j += 1
            ln[i] = j
            prev = i
    # (1.5 - 1.8)
    ss = [ln[i] for i in lms]
    if j < len(s) - 1:
        ss = suffix_array(ss)
    sorted_lms = [lms[ss[i]] for i in range(len(lms))]

    # phase 2: build suffix array
    sa = [None] * len(s)
    place_lms(sorted_lms, sa)
    place_l_positions(sa)
    place_s_positions(sa)
    return tuple(sa)


def lcp_array(s, sa):
    assert (len(s) == len(sa))
    isa = inverse_index_array(sa)
    lcp = [0] * len(s)
    l = 0
    for i in range(len(s)):
        j = isa[i]
        if j:
            k = sa[j - 1]
            while k + l < len(s) and i + l < len(s) and s[k + l] == s[i + l]:
                l += 1
            lcp[j] = l
            if l:
                l -= 1
    return tuple(lcp)


class LCPTreeNode(SimpleTreeNode):
    def __init__(self, lcp, lb, rb=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lcp = lcp
        self.lb = lb
        self.rb = rb


def bottom_up_lcp_interval_tree_traverse(lcp, action=None, keep_tree=False, node_class=LCPTreeNode):
    last_interval = None
    stack = list()
    stack.append(node_class(0, 0))
    for k in range(1, len(lcp) + 1):
        l = k - 1
        # close all interval on stack that ended at position k - 1
        while len(stack) and (k == len(lcp) or lcp[k] < stack[-1].lcp):
            stack[-1].rb = k
            last_interval = stack.pop()
            if action:
                action(last_interval)
            if not keep_tree:  # children are no more needed, so free the memory
                last_interval.children.clear()
            l = last_interval.lb
            if len(stack) and (k == len(lcp) or lcp[k] <= stack[-1].lcp):
                stack[-1].children.append(last_interval)
                last_interval = None
        if len(stack) and (k == len(lcp) or lcp[k] > stack[-1].lcp):  # open new interval
            stack.append(node_class(lcp[k], l))
            if last_interval is not None:
                stack[-1].children.append(last_interval)
                last_interval = None
    if keep_tree:
        return last_interval  # return root node
