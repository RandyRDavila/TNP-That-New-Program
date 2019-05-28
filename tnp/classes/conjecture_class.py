from fractions import Fraction

from tnp.functions.get_graph_data import get_graph_data


class Conjecture:
    def __init__(self, hyp, target, inequality, expression):
        self.hyp = hyp
        self.target = target
        self.inequality = inequality
        self.expression = expression.split()

    def get_expression(self):
        return " ".join(self.expression)

    def __str__(self):
        return f"If {self.hyp}, then {self.target} {self.inequality} {self.get_expression()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(hypothesis={self.hyp!r}, target={self.target!r}, inequality={self.inequality!r}, expression={self.get_expression()!r})"

    def target_value(self, G):
        # For now, we'll assume G is a dict or some object that implements __getitem__
        # In the future, though, it would be best to let G be a graph object so that
        # this is returning something like self.target(G), or looking up the value
        # from a database
        return G[self.target]

    def expression_value(self, G):
        # For now, we'll assume G is a dict or some object that implements __getitem__
        # In the future, though, it would best to let G be a graph object so
        # that G[invariant] becomes something like invariant(G), or looks up the
        # value from a database
        string = ""
        for invariant in self.expression:
            if invariant in G:
                string += str(G[invariant])
                string += " "
            else:
                string += invariant
                string += " "
        string += " +.0"
        try:
            return eval(string)
        except ZeroDivisionError:
            return 0

    def conjecture_instance(self, G):
        return eval(str(self.target_value(G)) + self.inequality() + str(self.expression_value(G)))

    def conjecture_sharp(self, G):
        return self.target_value(G) == self.expression_value(G)

    def sharp_graphs(self):
        graphs = get_graph_data()
        return [G for G in graphs if self.hyp(graphs[G]) is True and self.conjecture_sharp(graphs[G]) is True]

    def hyp_graphs(self):
        graphs = get_graph_data()
        return [G for G in graphs if self.hyp(graphs[G]) is True]

    def touch(self):
        return len(self.sharp_graphs())

    def scaled_touch(self):
        graphs = get_graph_data()
        graphs = [G for G in graphs if self.hyp(graphs[G]) is True]
        return Fraction(self.touch() / len(graphs)).limit_denominator(1000)

    def __eq__(self, other):
        if self.hyp == other.hyp:
            return self.get_expression() == other.get_expression()
        else:
            return False
