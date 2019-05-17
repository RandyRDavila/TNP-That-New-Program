from fractions import Fraction
from functions.get_graph_data import get_graph_data
from classes.conjecture_class import Conjecture




def make_ratio(hyp, target, invariant, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) == True]
    ratios = []
    for G in graphs:
        ratios.append(Fraction(G[target]/G[invariant]).limit_denominator(1000))
    if bound == "upper" and ratios != []:
        if max(ratios) == 1:
            return Conjecture(hyp, target, " <= ", f'{invariant}')
        else:
            return Conjecture(hyp, target, " <= ", f'{max(ratios)} * {invariant}')
    elif bound == "lower" and ratios != []:
        if min(ratios) == 1:
            return Conjecture(hyp, target, " >= ", f'{invariant}')
        else:
            return Conjecture(hyp, target, " >= ", f'{min(ratios)} * {invariant}')
    else:
        return None


def make_constant(hyp, target, invariant, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) == True]
    constants = []
    for G in graphs:
        constants.append(G[target] - G[invariant])
    if bound == "upper" and constants != []:
        if max(constants) == 0:
            return Conjecture(hyp, target, " <= ", f'{invariant}')
        else:
            return Conjecture(hyp, target, " <= ", f'{invariant} + {max(constants)}')
    elif bound == "lower" and constants != []:
        if min(constants) == 0:
            return Conjecture(hyp, target, " >= ", f'{invariant}')
        else:
            return Conjecture(hyp, target, " >= ", f'{invariant} + {min(constants)}')
    else:
        return None 




def make_ratios_two(hyp, target, invariant1, invariant2, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) == True]
    ratios = []
    for G in graphs:
        ratios.append(Fraction(G[target]/(G[invariant1] + G[invariant2])).limit_denominator(1000))
    if bound == "upper" and ratios != []:
        return Conjecture(hyp, target, " <= ", f'{max(ratios)} * ( {invariant1} + {invariant2} )')
    elif bound == "lower" and ratios != []:
        return Conjecture(hyp, target, " >= ", f'{min(ratios)} * ( {invariant1} + {invariant2} )')
    else:
        return None

def make_ratios_three(hyp, target, invariant1, invariant2, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) == True]
    ratios = []
    for G in graphs:
        if G[invariant1] != G[invariant2]:
            ratios.append(Fraction(G[target]/(G[invariant1] - G[invariant2])).limit_denominator(1000))
    if bound == "upper" and ratios != []:
        return Conjecture(hyp, target, " <= ", f'{max(ratios)} * ( {invariant1} - {invariant2} )')
    elif bound == "lower" and ratios != []:
        return Conjecture(hyp, target, " >= ", f'{min(ratios)} * ( {invariant1} - {invariant2} )')
    else:
        return None

def make_ratios_four(hyp, target, invariant1, invariant2, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) == True]
    ratios = []
    for G in graphs:
        if G[invariant1] != G[invariant2]:
            ratios.append(Fraction((G[target]*(G[invariant1])/G[invariant2])).limit_denominator(1000))
    if bound == "upper" and ratios != []:
        return Conjecture(hyp, target, " <= ", f'{max(ratios)} * ( {invariant2} / {invariant1} )')
    elif bound == "lower" and ratios != []:
        return Conjecture(hyp, target, " >= ", f'{min(ratios)} * ( {invariant2} / {invariant1} )')
    else:
        return None


def make_ratios_five(hyp, target, invariant1, invariant2, invariant3, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) == True]
    ratios = []
    for G in graphs:
        if G[invariant1] != G[invariant2]:
            ratios.append(Fraction((G[target]*(G[invariant1])/(G[invariant2])+G[invariant3])).limit_denominator(1000))
    if bound == "upper" and ratios != []:
        return Conjecture(hyp, target, " <= ", f'{max(ratios)} * ( {invariant2} + {invariant3} ) / {invariant1}')
    elif bound == "lower" and ratios != []:
        return Conjecture(hyp, target, " >= ", f'{min(ratios)} * ( {invariant2} + {invariant3} ) / {invariant1}')
    else:
        return None




    

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

