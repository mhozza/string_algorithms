from .tree import TreeNode, Tree


class TrieNode(TreeNode):
    def __init__(self, is_word=False, *args, **kwargs):
        super(TrieNode, self).__init__()
        self.is_word = is_word

    def add(self, char, is_word=False, *args, **kwargs):
        return super(TrieNode, self).add(char, is_word)


class Trie(Tree):
    def __init__(self, node_class=TrieNode, *args, **kwargs):
        super(Trie, self).__init__(node_class=node_class, *args, **kwargs)

    def add(self, word, *args, **kwargs):
        node = self.root
        for c in word:
            node = node.add(c, False, *args, **kwargs)
        node.is_word = True
        return node

    def get_node(self, word):
        node = self.root
        for c in word:
            node = node.get(c)
            if node is None:
                break
        return node

    def find(self, word):
        node = self.get_node(word)
        return node is not None and node.is_word

    def is_prefix(self, word):
        return self.get_node(word) is not None
