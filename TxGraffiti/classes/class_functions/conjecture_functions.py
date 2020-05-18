from fractions import Fraction
from sympy import sympify
from TxGraffiti.functions.get_graph_data import get_graph_data



def hyp_graphs(conj, family = 'test_data'):
        graphs = get_graph_data(family)
        return [G for G in graphs if conj.hyp(graphs[G]) is True]



def conjecture_test(conj, test_family = 'test_data'):
    return False not in [conj(G) for G in hyp_graphs(conj, family = test_family)]



def sharp_graphs(conj, test_family = 'test_data', graphs = []):
    if graphs == []:
        graphs = hyp_graphs(conj, family = test_family)
        return [G for G in graphs if conj.conjecture_sharp(graphs[G]) is True]
    else:
        return [G for G in graphs 
                if conj.hyp(graphs[G]) is True 
                and conj.conjecture_sharp(graphs[G]) is True]


def touch(conj, test_family = 'test_data', graphs = []):
    if graphs == []:
        graphs = hyp_graphs(conj, family = test_family)
        return len([G for G in graphs if conj.conjecture_sharp(graphs[G]) is True])
    else:
        return len([G for G in graphs 
                if conj.hyp(graphs[G]) is True 
                and conj.conjecture_sharp(graphs[G]) is True])




