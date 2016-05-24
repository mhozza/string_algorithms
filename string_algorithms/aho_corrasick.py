from collections import deque

from .trie import Trie, TrieNode


class ACNode(TrieNode):
    def __init__(self, *args, **kwargs):
        super(ACNode, self).__init__(*args, **kwargs)
        self.output = set()
        self.fail = None


def preprocess(patterns):
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
                node.output = set([node]) | node.fail.output
            else:
                # copy output from fail link
                node.output = set(node.fail.output)
            q.append(node)
    return t, pattern_map


def find(patterns, text):
    t, pattern_map = preprocess(patterns)
    results = []
    node = t.root
    for i, c in enumerate(text):
        while node != t.root and c not in node.children:
            node = node.fail
        if c in node.children:
            node = node.get(c)
            results += [(i - len(pattern_map[o]) + 1, pattern_map[o]) for o in node.output]
    return results
