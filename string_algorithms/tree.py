class TreeNode:
    def __init__(self, *args, **kwargs):
        self.children = dict()

    def get(self, key):
        return self.children.get(key, None)

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


def preorder_traversal(tree, action=None, sort=False):
    return euler_tour(tree, pre_action=action, sort=sort)


def euler_tour(tree, action=None, pre_action=None, post_action=None, sort=False):
    if action is not None and pre_action is not None or post_action is not None:
        raise AttributeError('Cannot set both action and pre_action or post_action')

    if action is not None and pre_action is None and post_action is None:
        pre_action = post_action = action

    visited = set()

    def visit(node, depth=0):
        if node in visited:
            return
        visited.add(node)
        if pre_action:
            pre_action(node, depth)
        children = sorted(node.children.values()) if sort else node.children.values()
        for n in children:
            visit(n, depth+1)
            if post_action:
                post_action(node, depth)

    node = tree.root
    visit(node)
