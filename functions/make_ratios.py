from fractions import Fraction
from functions.get_graph_data import get_graph_data
from classes.hypothesis_class import hypothesis
from classes.conclusion_class import conclusion
from classes.conjecture_class import conjecture


def make_ratio(hyp, target, invariant, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) == True]
    ratios = []
    for G in graphs:
        ratios.append(Fraction(G[target]/G[invariant]).limit_denominator(1000))
    if bound == "upper":
        return conjecture(hyp, conclusion(target, invariant, "<=", max(ratios), 0))
    else:
        return conjecture(hyp, conclusion(target, invariant, ">=", min(ratios), 0))


def make_constant(hyp, target, invariant, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) == True]
    constants = []
    for G in graphs:
        if G[target] - G[invariant] != 0:
            constants.append(G[target] - G[invariant])
    if bound == "upper":
        return conjecture(hyp, conclusion(target, invariant, "<=", 1, max(constants)))
    else:
        return conjecture(hyp, conclusion(target, invariant, ">=", 1, min(constants)))





def make_ratios_two(hypothesis, target, invariant1, invariant2):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if graphs[G][hypothesis] == True]
    ratios = []
    for G in graphs:
        ratios.append(Fraction(G[target]/(G[invariant1] + G[invariant2])).limit_denominator(1000))
    return hypothesis, target, invariant1, invariant2, min(ratios), max(ratios)

def make_ratios_three(hypothesis, target, invariant1, invariant2):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if graphs[G][hypothesis] == True]
    ratios = []
    for G in graphs:
        if G[invariant1] != G[invariant2]:
            ratios.append(Fraction(G[target]/(G[invariant1] - G[invariant2])).limit_denominator(1000))
    return hypothesis, target, invariant1, invariant2, min(ratios), max(ratios)

def make_ratios_four(hypothesis, target, invariant1, invariant2):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if graphs[G][hypothesis] == True]
    ratios = []
    for G in graphs:
        if G[invariant1] != G[invariant2]:
            ratios.append(Fraction((G[target]*(G[invariant1])/G[invariant2])).limit_denominator(1000))
    return hypothesis, target, invariant1, invariant2, min(ratios), max(ratios)


def make_ratios_five(hypothesis, target, invariant1, invariant2, invariant3):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if graphs[G][hypothesis] == True]
    ratios = []
    for G in graphs:
        if G[invariant1] != G[invariant2]:
            ratios.append(Fraction((G[target]*(G[invariant1])/(G[invariant2])+G[invariant3])).limit_denominator(1000))
    return hypothesis, target, invariant1, invariant2, invariant3, min(ratios), max(ratios)




    

def make_constant_two(hypothesis, target, invariant):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if graphs[G][hypothesis] == True]
    constants = []
    for G in graphs:
        constants.append(G[target] + G[invariant])
    return hypothesis, target, invariant, min(constants), max(constants)

def make_constant_three(hypothesis, target, invariant1, invariant2):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if graphs[G][hypothesis] == True]
    constants = []
    for G in graphs:
        constants.append(G[target] - G[invariant1] - G[invariant2])
    return hypothesis, target, invariant1, invariant2, min(constants), max(constants)

def make_constant_four(hypothesis, target, invariant1, invariant2):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if graphs[G][hypothesis] == True]
    constants = []
    for G in graphs:
        constants.append(G[target] - G[invariant1] + G[invariant2])
    return hypothesis, target, invariant1, invariant2, min(constants), max(constants)

