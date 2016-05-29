class TreeNode:
    def __init__(self, **kwargs):
        self.children = dict()

    def get(self, key):
        return self.children.get(key, None)

    def get_children(self, sort=False):
        if sort:
            return sorted(self.children.values())
        return self.children.values()

    def add(self, key, node=None, **kwargs):
        if key not in self.children:
            if node is None:
                node = self.__class__(**kwargs)
            self.children[key] = node
        return self.children[key]

    def set(self, key, val, **kwargs):
        self.children[key] = val
        return self.children[key]


class OrderedTreeNode:
    def __init__(self, **kwargs):
        self.children = list()

    def get(self, index):
        return self.children[index]

    def get_children(self, sort=False):
        if sort:
            return sorted(self.children)
        return self.children

    def add(self, node=None, **kwargs):
        if node is None:
            node = self.__class__(**kwargs)
        self.children.append(node)
        return self.children[-1]

    def set(self, index, val, **kwargs):
        self.children[index] = val
        return self.children[index]


class Tree:
    def __init__(self, root=None, node_class=TreeNode, **kwargs):
        if root is None:
            root = node_class(**kwargs)
        self.root = root
        self.node_class = node_class

    def get_children(self, node, sort=False):
        return node.get_children(sort=sort)

    def dfs(self, action=None, pre_action=None, post_action=None, sort=False):
        assert(action is None or (pre_action is None and post_action is None))
        if action is not None and pre_action is None and post_action is None:
            pre_action = post_action = action

        def visit(node, depth=0, parent=None):
            if pre_action:
                if pre_action(node, depth, parent):
                    return
            for n in self.get_children(node, sort=sort):
                visit(n, depth+1, node)
                if post_action:
                    if post_action(node, depth, parent):
                        return

        visit(self.root)
