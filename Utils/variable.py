class Variable:
    def __init__(self, index):
        self.index = index

    def __eq__(self, other):
        return isinstance(other, Variable) and self.index == other.index

    def __hash__(self):
        return hash(self.index)