import pickle
from sympy import sympify
from functions.get_graph_data import get_graph_data


class Conjecture:

    def __init__(self, hyp, target, inequality, expression):
        self.hyp = hyp
        self.target = target
        self.inequality = inequality
        self.expression = expression.split()


    def get_expression(self):
        s = ''
        for string in self.expression:
            s+= string
            s+= ' '
        return s


    def get_string(self):
        return f'{self.target} {self.inequality} {sympify(self.get_expression())}'


    def __repr__(self):
        return f'If {self.hyp}, then {self.get_string()}'


    def target_value(self, G):
        return G[self.target]


    def expression_value(self, G):
        string = ''
        for invariant in self.expression:
            if invariant in G:
                string += str(G[invariant])
                string += ' '
            else:
                string += invariant
                string += ' '
        string +=' +.0'
        try: return eval(string)
        except ZeroDivisionError: return 0


    def conjecture_instance(self, G):
        return eval(str(self.target_value(G))+self.inequality()+
                    str(self.expression_value(G)))


    def conjecture_sharp(self, G):
        return self.target_value(G) == self.expression_value(G)


    def sharp_graphs(self):
        graphs = get_graph_data()
        len([graphs[G] for G in graphs if self.hyp(graphs[G]) == True])


    def touch(self):
        graphs = get_graph_data()
        graphs = [graphs[G] for G in graphs if self.hyp(graphs[G]) == True]
        return len([G for G in graphs if self.conjecture_sharp(G) == True])


    def scaled_touch(self):
        graphs = get_graph_data()
        graphs = [graphs[G] for G in graphs if self.hyp(graphs[G]) == True]
        return self.touch()/len(graphs)


    def __eq__(self, other):
        if self.get_expression() == other.get_expression():
            return True
        else:
            return False

    def is_more_general(self, other):
        if self.get_expression() == other.get_expression():
            return set(other.hyp).issubset(set(self.hyp))
        else:
            return False
