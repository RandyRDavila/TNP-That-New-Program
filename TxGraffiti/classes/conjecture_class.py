from fractions import Fraction
from sympy import sympify
from TxGraffiti.functions.get_graph_data import get_graph_data


class Conjecture:
    """
    A class to represent a conjecture. Here conjectures are conditional statements of the form

        If G satisfies hyp, then target inequality expression. 

    ...

    Attributes
    ----------
    hyp : hypothesis class
        A hypothesis for a given conditional statement.

    target : str
        A graph invariant for for which a conjecture is made on.

    inequality : str
        Either 'upper' or 'lower' to decide the direction of the inequality against target.

    expression : str
        A combination of graph invariants and operations on said graph invariants. 


    Methods
    -------
    get_expression():
        Returns the string representation of the conjectures expression.

    get_string():
        Returns the string representation of the entire conjectures.

    target_value(G):
        Returns the numeric value of the target invariant on a specific graph G.

    expression_value(G):
        Returns the numeric value of the expression evaluated on a specific graph G.

    conjecture_instance(G):
        Returns a boolean value for the conjecture instance on a specified graph G.

    conjecture_sharp(G):
        Returns a boolean value for the conjecture holding with equality on a specified graph G.

    sharp_graphs(family = 'test_data', graphs = []):
        Returns the set of all sharp graphs. 

    hyp_graphs(family = 'test_data', graphs = []):
        Returns the set of all graphs satisfying the hypothesis. 

    touch():
        Returns the number of times the conjecture holds with equality. 
    """



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

    def __call__(self, G):
        return eval(str(self.target_value(G)) + self.inequality() + str(self.expression_value(G)))

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
        return Fraction(self.touch() / len(graphs)).limit_denominator(1000)

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

    def __le__(self, other):
        if self.target == other.target and self.get_expression() == other.get_expression():
            return set(self.hyp_graphs()) <= set(other.hyp_graphs())
        else:
            return False   

        

