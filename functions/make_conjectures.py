from fractions import Fraction
from functions.get_graph_data import get_graph_data


def make_ratio(hyp, target, invariant, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) == True]
    ratios = []
    for G in graphs:
        ratios.append(Fraction(G[target] / G[invariant]).limit_denominator(1000))
    if bound == "upper":
        return hyp, target, "<=", max(ratios), "*", invariant
    else:
        return hyp, target, ">=", min(ratios), "*", invariant


def make_constant(hyp, target, invariant, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) == True]
    constants = []
    for G in graphs:
        if G[target] - G[invariant] != 0:
            constants.append(G[target] - G[invariant])
    if bound == "upper":
        return hyp, target, invariant, "<=", invariant, "+", max(constants)
    else:
        return hyp, target, invariant, ">=", invariant, "+", min(constants)

