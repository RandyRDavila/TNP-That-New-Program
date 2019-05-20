from fractions import Fraction

from tnp.classes.conjecture_class import Conjecture
from tnp.functions.get_graph_data import get_graph_data


def make_ratio(hypotheses, target, invariant, bound):
    bound = bound.lower()
    if bound not in ("upper", "lower"):
        raise ValueError("bound must be one of 'upper' or 'lower'")

    graph_data = get_graph_data()
    graphs_satisfying_hypotheses = (graph_data[G] for G in graph_data if hypotheses(graph_data[G]) is True)
    ratios = tuple(Fraction(G[target] / G[invariant]).limit_denominator(1000) for G in graphs_satisfying_hypotheses)
    if ratios == ():
        return None

    inequality_symbol = " <= " if bound == "upper" else " >= "
    ratio = max(ratios) if bound == "upper" else min(ratios)
    right_hand_side = f"{invariant}" if ratio == 1 else f"{ratio} * {invariant}"
    return Conjecture(hypotheses, target, inequality_symbol, right_hand_side)


def make_constant(hypotheses, target, invariant, bound):
    bound = bound.lower()
    if bound not in ("upper", "lower"):
        raise ValueError("bound must be one of 'upper' or 'lower'")

    graph_data = get_graph_data()
    graphs_satisfying_hypotheses = (graph_data[G] for G in graph_data if hypotheses(graph_data[G]) is True)
    constants = tuple(G[target] - G[invariant] for G in graphs_satisfying_hypotheses)
    if constants == ():
        return None

    inequality_symbol = " <= " if bound == "upper" else " >= "
    constant = max(constants) if bound == "upper" else min(constants)
    right_hand_side = f"{invariant}" if constant == 0 else f"{invariant} + {constant}"
    return Conjecture(hypotheses, target, inequality_symbol, right_hand_side)


def make_constant_two(hyp, target, invariant1, invariant2, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) is True]
    constants = []
    for G in graphs:
        constants.append(G[target] - (G[invariant1] / G[invariant2]))
    if bound == "upper" and constants != []:
        if max(constants) == 0:
            return Conjecture(hyp, target, " <= ", f"{invariant1} / {invariant2}")
        else:
            return Conjecture(hyp, target, " <= ", f"( {invariant1} / {invariant2} ) + {max(constants)}")
    elif bound == "lower" and constants != []:
        if min(constants) == 0:
            return Conjecture(hyp, target, " >= ", f"{invariant1} / {invariant2}")
        else:
            return Conjecture(hyp, target, " >= ", f"( {invariant1} / {invariant2} ) + {min(constants)}")
    else:
        return None


def make_ratio_two(hyp, target, invariant1, invariant2, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) is True]
    ratios = []
    for G in graphs:
        ratios.append(Fraction(G[target] / (G[invariant1] + G[invariant2])).limit_denominator(1000))
    if bound == "upper" and ratios != []:
        if max(ratios) == 1:
            return Conjecture(hyp, target, " <= ", f"{invariant1} + {invariant2}")
        else:
            return Conjecture(hyp, target, " <= ", f"{max(ratios)} * ( {invariant1} + {invariant2} )")
    elif bound == "lower" and ratios != []:
        if min(ratios) == 1:
            return Conjecture(hyp, target, " >= ", f"{invariant1} + {invariant2}")
        else:
            return Conjecture(hyp, target, " >= ", f"{min(ratios)} * ( {invariant1} + {invariant2} )")
    else:
        return None


def make_ratio_three(hyp, target, invariant1, invariant2, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) is True]
    ratios = []
    for G in graphs:
        if G[invariant1] != G[invariant2]:
            ratios.append(Fraction((G[target] * (G[invariant1]) / G[invariant2])).limit_denominator(1000))
    if bound == "upper" and ratios != []:
        if max(ratios) == 1:
            return Conjecture(hyp, target, " <= ", f"{invariant2} / {invariant1}")
        else:
            return Conjecture(hyp, target, " <= ", f"{max(ratios)} * ( {invariant2} / {invariant1} )")
    elif bound == "lower" and ratios != []:
        if min(ratios) == 1:
            return Conjecture(hyp, target, " >= ", f"{invariant2} / {invariant1}")
        else:
            return Conjecture(hyp, target, " >= ", f"{min(ratios)} * ( {invariant2} / {invariant1} )")
    else:
        return None
