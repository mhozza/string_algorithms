class TrieNode():
    def __init__(self, is_word=False, *args, **kwargs):
        self.children = dict()
        self.is_word = is_word

    def next(self, char):
        return self.children.get(char, None)

    def add(self, char, is_word=False, *args, **kwargs):
        if char not in self.children:
            self.children[char] = self.__class__(is_word, *args, **kwargs)
        return self.children[char]


class Trie():
    def __init__(self, node_class=TrieNode, *args, **kwargs):
        self.root = node_class(*args, **kwargs)

    def add(self, word, *args, **kwargs):
        node = self.root
        for c in word:
            node = node.add(c, False, *args, **kwargs)
        node.is_word = True
        return node

    def get_node(self, word):
        node = self.root
        for c in word:
            node = node.next(c)
            if node is None:
                break
        return node

    def find(self, word):
        node = self.get_node(word)
        return node is not None and node.is_word

    def is_preffix(self, word):
        return self.get_node(word) is not None
