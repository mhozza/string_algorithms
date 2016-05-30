from collections import deque

from string_algorithms.suffix_array import lcp_array, LCPConceptualIntervalTree
from string_algorithms.suffix_array import suffix_array
from .trie import Trie, TrieNode


def naive_find(pattern, text):
    results = []
    for i in range(len(text) - len(pattern)):
        found = True
        for j, p in enumerate(pattern):
            if text[i + j] != p:
                found = False
                break
        if found:
            results.append(i)
    return results


def kmp_preprocess(pattern):
    p = [0] * len(pattern)
    for i in range(1, len(pattern)):
        j = p[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = p[j - 1]
        if pattern[i] == pattern[j]:
            p[i] = j + 1
    return p


def kmp(pattern, text):
    p = kmp_preprocess(pattern)
    results = []
    j = 0
    for i, c in enumerate(text):
        while j > 0 and c != pattern[j]:
            j = p[j - 1]
        if c == pattern[j]:
            if j == len(pattern) - 1:
                results.append(i - j)
                j = p[j - 1]
            else:
                j += 1
    return results


class ACNode(TrieNode):
    def __init__(self, *args, **kwargs):
        super(ACNode, self).__init__(*args, **kwargs)
        self.output = set()
        self.fail = None


def aho_corrasick_preprocess(patterns):
    pattern_map = dict()
    t = Trie(node_class=ACNode)
    for pattern in patterns:
        pattern_map[t.add(pattern)] = pattern
    q = deque([t.root])

    # BFS through the Trie
    while q:
        parent = q.popleft()
        for c, node in parent.children.items():
            fail = parent.fail
            while fail and fail != t.root and c not in fail.children:
                fail = fail.fail
            if fail and c in fail.children:
                node.fail = fail.children[c]
            else:
                node.fail = t.root
            if node.is_word:
                node.output = {node} | node.fail.output
            else:
                # copy output from fail link
                node.output = set(node.fail.output)
            q.append(node)
    return t, pattern_map


def aho_corrasick(patterns, text):
    t, pattern_map = aho_corrasick_preprocess(patterns)
    results = []
    node = t.root
    for i, c in enumerate(text):
        while node != t.root and c not in node.children:
            node = node.fail
        if c in node.children:
            node = node.get(c)
            results += [(i - len(pattern_map[o]) + 1, pattern_map[o]) for o in node.output]
    return results


def sa_preprocess(text):
    sa = suffix_array(text)
    lcp = lcp_array(text, sa)
    lcptree = LCPConceptualIntervalTree(lcp, include_singletons=True)
    return text, sa, lcptree


def suffix_array_match(pattern, sa_preprocessed_text, sort=False):
    text, sa, lcptree = sa_preprocessed_text
    current_pos = 0
    interval = None

    def pre_action(node, *_):
        nonlocal interval
        nonlocal current_pos
        if node.lcp is None:
            d = len(pattern) - current_pos
        else:
            d = min(len(pattern), node.lcp) - current_pos
        if (
            interval is not None or
            pattern[current_pos:current_pos + d] != text[current_pos + sa[node.lb]:current_pos + sa[node.lb] + d]
        ):
            # this interval does not contain pattern, so skip it
            return True
        current_pos += d
        if current_pos == len(pattern):
            interval = node
            return True

    lcptree.dfs(pre_action=pre_action)
    if interval is None:
        return []
    positions = [sa[i] for i in range(interval.lb, interval.rb)]
    return sorted(positions) if sort else positions
