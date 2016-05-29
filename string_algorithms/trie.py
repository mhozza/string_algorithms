from .tree import Tree, TreeNode


class TrieNode(TreeNode):
    def __init__(self, is_word=False, **kwargs):
        super(TrieNode, self).__init__()
        self.is_word = is_word

    def add(self, char, node=None, is_word=False, **kwargs):
        return super(TrieNode, self).add(char, node, is_word=is_word)


class Trie(Tree):
    def __init__(self, root=None, node_class=TrieNode, **kwargs):
        super(Trie, self).__init__(root=root, node_class=node_class, **kwargs)

    def add(self, word, **kwargs):
        node = self.root
        for c in word:
            node = node.add(c, is_word=False, **kwargs)
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
