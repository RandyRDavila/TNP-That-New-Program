from fractions import Fraction
from functions.get_graph_data import get_graph_data
from classes.conjecture_class import type_one_conjecture


def make_ratio(hyp, target, invariant, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) == True]
    ratios = []
    for G in graphs:
        ratios.append(Fraction(G[target] / G[invariant]).limit_denominator(100000))
    if bound == "upper" and ratios != []:
        return type_one_conjecture(hyp, target, "<=", max(ratios), "*", invariant)
    elif bound == "lower" and ratios != []:
        return type_one_conjecture(hyp, target, ">=", min(ratios), "*", invariant)
    else:
        return None


def make_constant(hyp, target, invariant, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) == True]
    constants = []
    for G in graphs:
        constants.append(G[target] - G[invariant])
    if bound == "upper" and constants != []:
        return type_one_conjecture(hyp, target, "<=", max(constants), "+", invariant)
    elif bound == "lower" and constants != []:
        return type_one_conjecture(hyp, target, ">=", min(constants), "+", invariant)
    else:
        return None


