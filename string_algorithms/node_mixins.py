class LabeledOrderedNodeMixin:
    def __init__(self, label, **kwargs):
        self.label = label
        super(LabeledOrderedNodeMixin, self).__init__(**kwargs)

    def __str__(self):
        return str(self.label)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.label)

    def __lt__(self, other):
        return self.label < other.label


class LabeledNodeMixin(LabeledOrderedNodeMixin):
    def add(self, key, node=None, label=None, **kwargs):
        if label is None:
            label = key
        return super(LabeledNodeMixin, self).add(key, node, label=label, **kwargs)
