from fractions import Fraction

from tnp.classes.conjecture_class import Conjecture
from tnp.functions.get_graph_data import get_graph_data


def make_ratio(hyp, target, invariant, bound):
    """
    Parameters
    ----------
    hyp : hypothesis object

    target : graph invariant to conjecture on

    invariant : graph invariant to compare with target

    bound : 'upper' or 'lower', indicating direction of inequality
    
    
    Returns
    -------
    conjecture instance:
          

    If bound == 'upper', then returns the following conjecture instance: 
    'If G satisfies hyp, then target(G) <= C*invariant(G)' 
    where C = max{target(G)/invariant(G): G is in the graph database}
          
    If bound == 'lower', then returns the following conjecture instance:
    'If G satisfies hyp, then target(G) >= C*invariant(G)',
    where C = min{target(G)/invariant(G): G is in the graph database}.

    """

    graphs = get_graph_data() # Collect graph data
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) is True]  # Only consider graphs satisfying the specified hypothesis
    ratios = [] # Store possible ratios
    for G in graphs:
        ratios.append(Fraction(G[target] / G[invariant]).limit_denominator(1000))
    
    if bound == "upper" and ratios != []:
        if max(ratios) == 1:
            return Conjecture(hyp, target, " <= ", f"{invariant}")
        else:
            return Conjecture(hyp, target, " <= ", f"{max(ratios)} * {invariant}")
    
    elif bound == "lower" and ratios != []:
        if min(ratios) == 1:
            return Conjecture(hyp, target, " >= ", f"{invariant}")
        else:
            return Conjecture(hyp, target, " >= ", f"{min(ratios)} * {invariant}")


def make_constant(hyp, target, invariant, bound):
    """
    Parameters
    ----------
    hyp : hypothesis object

    target : graph invariant to conjecture on

    invariant : graph invariant to compare with target

    bound : 'upper' or 'lower', indicating direction of inequality
    
    
    Returns
    -------
    conjecture instance:
          

    If bound == 'upper', then returns the following conjecture instance: 
    'If G satisfies hyp, then target(G) <= invariant(G) + C' 
    where C = max{target(G) - invariant(G): G is in the graph database}
          
    If bound == 'lower', then returns the following conjecture instance:
    'If G satisfies hyp, then target(G) >= invariant(G) + C',
    where C = min{target(G) - invariant(G): G is in the graph database}.

    """

    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) is True]
    constants = []
    for G in graphs:
        constants.append(G[target] - G[invariant])
    if bound == "upper" and constants != []:
        if max(constants) == 0:
            return Conjecture(hyp, target, " <= ", f"{invariant}")
        else:
            return Conjecture(hyp, target, " <= ", f"{invariant} + {max(constants)}")
    elif bound == "lower" and constants != []:
        if min(constants) == 0:
            return Conjecture(hyp, target, " >= ", f"{invariant}")
        else:
            return Conjecture(hyp, target, " >= ", f"{invariant} + {min(constants)}")


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


def make_ratio_four(hyp, target, invariant1, invariant2, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) is True]
    ratios = []
    for G in graphs: 
        ratios.append(Fraction(G[target] / (G[invariant1] - G[invariant2])).limit_denominator(1000))
    if bound == "upper" and ratios != []:
        if max(ratios) == 1:
            return Conjecture(hyp, target, " <= ", f"{invariant1} - {invariant2}")
        else:
            return Conjecture(hyp, target, " <= ", f"{max(ratios)} * ( {invariant1} - {invariant2} )")
    elif bound == "lower" and ratios != []:
        if min(ratios) == 1:
            return Conjecture(hyp, target, " >= ", f"{invariant1} - {invariant2}")
        else:
            return Conjecture(hyp, target, " >= ", f"{min(ratios)} * ( {invariant1} - {invariant2} )")
    else:
        return None



def make_ratio_five(hyp, target, invariant1, invariant2, invariant3, bound):
    graphs = get_graph_data()
    graphs = [graphs[G] for G in graphs if hyp(graphs[G]) is True]
    ratios = []
    for G in graphs:
        if G[invariant1] != G[invariant2]:
            ratios.append(Fraction((G[target] * (G[invariant1]) / (G[invariant2]*G[invariant3]))).limit_denominator(1000))
    if bound == "upper" and ratios != []:
        if max(ratios) == 1:
            return Conjecture(hyp, target, " <= ", f"{invariant2} * {invariant3} / {invariant1}")
        else:
            return Conjecture(hyp, target, " <= ", f"{max(ratios)} * ( {invariant2} * {invariant3} / {invariant1} )")
    elif bound == "lower" and ratios != []:
        if min(ratios) == 1:
            return Conjecture(hyp, target, " >= ", f"{invariant2} * {invariant3} / {invariant1}")
        else:
            return Conjecture(hyp, target, " >= ", f"{min(ratios)} * ( {invariant2} * {invariant3} / {invariant1} )")
    else:
        return None