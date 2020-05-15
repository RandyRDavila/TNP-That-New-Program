from fractions import Fraction

from sympy import sympify

from TxGraffiti.functions.get_graph_data import get_graph_data


class Conjecture:
    def __init__(self, hyp, target, inequality, expression):
        self.hyp = hyp
        self.target = target
        self.inequality = inequality
        self.expression = expression.split()

    def get_expression(self):
        s = ""
        for string in self.expression:
            s += string
            s += " "
        return s

    def get_string(self):
        return f"{self.target} {self.inequality} {sympify(self.get_expression())}"

    def __repr__(self):
        return f"If {self.hyp}, then {self.target} {self.inequality} {self.get_expression()}"

    def target_value(self, G):
        return G[self.target]

    def expression_value(self, G):
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

    def sharp_graphs(self, family = 'test_data', graphs = []):
        if graphs == []:
            graphs = get_graph_data(family)
            return [G for G in graphs 
                    if self.hyp(graphs[G]) is True 
                    and self.conjecture_sharp(graphs[G]) is True]
        else:
            return [G for G in graphs 
                    if self.hyp(graphs[G]) is True 
                    and self.conjecture_sharp(graphs[G]) is True]

    def hyp_graphs(self, family = 'test_data'):
        graphs = get_graph_data(family)
        return [G for G in graphs if self.hyp(graphs[G]) is True]

    def touch(self):
        return len(self.sharp_graphs())

    def scaled_touch(self, family = 'test_data'):
        graphs = get_graph_data(family)
        graphs = [G for G in graphs if self.hyp(graphs[G]) is True]
        return Fraction(self.touch(family) / len(graphs)).limit_denominator(1000)

    def __eq__(self, other):
        if self.hyp == other.hyp:
            return self.get_expression() == other.get_expression()
        else:
            return False

    def __ge__(self, other):
        if self.target == other.target and self.get_expression() == other.get_expression():
            return set(self.hyp_graphs()) >= set(other.hyp_graphs())
        else:
            return False

    def __le__(self, other, family):
        if self.target == other.target and self.get_expression() == other.get_expression():
            return set(self.hyp_graphs()) <= set(other.hyp_graphs())
        else:
            return False   

        

