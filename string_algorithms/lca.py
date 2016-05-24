from .tree import euler_tour
from .rmq import RMQ


class LCA:
    def __init__(self, tree):
        self.tree = tree
        self.euler_tour = []
        self.depths = []
        self.representative = dict()
        euler_tour(self.tree, self.compute_arrays_action)
        self.compute_representatives()
        self.rmq = RMQ(self.depths)

    def compute_arrays_action(self, node, depth):
        self.euler_tour.append(node)
        self.depths.append(depth)

    def compute_representatives(self):
        for i, n in enumerate(self.euler_tour):
            if n not in self.representative:
                self.representative[n] = i

    def query(self, a, b):
        return self.euler_tour[self.rmq.query(self.representative[a], self.representative[b])]
