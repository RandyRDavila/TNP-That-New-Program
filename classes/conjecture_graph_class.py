

class conjecture_graph:

    def __init__(self, networkx_graph, name):
        self.Graph = networkx_graph
        self.name = name

    def __repr__(self):
        return self.name

    