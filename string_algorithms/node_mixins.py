class LabeledSimpleNodeMixin:
    def __init__(self, label, *args, **kwargs):
        self.label = label
        super(LabeledSimpleNodeMixin, self).__init__(*args, **kwargs)

    def __str__(self):
        return str(self.label)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.label)


class LabeledNodeMixin(LabeledSimpleNodeMixin):
    def add(self, key, label=None, *args, **kwargs):
        if label is None:
            label = key
        return super(LabeledNodeMixin, self).add(key, label=label)

    def __lt__(self, other):
        return self.label < other.label
