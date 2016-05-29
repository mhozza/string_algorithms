class TreeNode:
    def __init__(self, *args, **kwargs):
        self.children = dict()

    def get(self, key):
        return self.children.get(key, None)

    def get_children(self, sort=False):
        if sort:
            return sorted(self.children.values())
        return self.children.values()

    def add(self, key, node=None, *args, **kwargs):
        if key not in self.children:
            if node is None:
                node = self.__class__(*args, **kwargs)
            self.children[key] = node
        return self.children[key]

    def set(self, key, val, *args, **kwargs):
        self.children[key] = val
        return self.children[key]


class OrderedTreeNode:
    def __init__(self, *args, **kwargs):
        self.children = list()

    def get(self, index):
        return self.children[index]

    def get_children(self, sort=False):
        if sort:
            return sorted(self.children)
        return self.children

    def add(self, node=None, *args, **kwargs):
        if node is None:
            node = self.__class__(*args, **kwargs)
        self.children.append(node)
        return self.children[-1]

    def set(self, index, val, *args, **kwargs):
        self.children[index] = val
        return self.children[index]


class Tree:
    def __init__(self, node_class=TreeNode, *args, **kwargs):
        self.root = node_class(*args, **kwargs)


def dfs(tree, action=None, pre_action=None, post_action=None, sort=False):
    assert(action is None or pre_action is None and post_action is None)
    if action is not None and pre_action is None and post_action is None:
        pre_action = post_action = action
    visited = set()

    def visit(node, depth=0):
        if node in visited:
            return
        visited.add(node)
        if pre_action:
            pre_action(node, depth)
        for n in node.get_children(sort=sort):
            visit(n, depth+1)
            if post_action:
                post_action(node, depth)
    visit(tree.root)
