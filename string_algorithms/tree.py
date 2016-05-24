class TreeNode:
    def __init__(self, *args, **kwargs):
        self.children = dict()

    def get(self, index):
        return self.children[index]

    def add(self, key, *args, **kwargs):
        if key not in self.children:
            self.children[key] = self.__class__(*args, **kwargs)
        return self.children[key]

    def set(self, key, val, *args, **kwargs):
        self.children[key] = val
        return self.children[key]


class BinaryNode(TreeNode):
    @property
    def left(self):
        return self.get(0)

    @left.setter
    def left(self, val):
        self.set(0, val)

    @property
    def right(self):
        return self.get(1)

    @right.setter
    def right(self, val):
        self.set(1, val)


class Tree:
    def __init__(self, node_class=TreeNode, *args, **kwargs):
        self.root = node_class(*args, **kwargs)


class BinaryTree(Tree):
    def __init__(self, node_class=BinaryNode, *args, **kwargs):
        super(BinaryTree, self).__init__(node_class=node_class, *args, **kwargs)


def preorder_traversal(tree, action=lambda n, d: None):
    visited = set()

    def visit(node, depth=0):
        if node in visited:
            return
        visited.add(node)
        action(node, depth)
        for n in node.children.values():
            visit(n, depth+1)

    node = tree.root
    visit(node)
