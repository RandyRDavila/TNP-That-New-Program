from fractions import Fraction
from TxGraffiti.classes.conjecture_class import Conjecture
from TxGraffiti.functions.get_graph_data import get_graph_data


__all__ = ['make_ratio',
            'make_constant',
            'make_ratio_two',
            'make_constant_two', 
            'make_ratio_three',
            'make_ratio_four']



def make_ratio(graphs, hyp, target, invariant):
    """
    Parameters
    ----------
    graphs : dictionary of graphs with precomputed graph properties

    hyp : hypothesis object

    target : graph invariant to conjecture on

    invariant : graph invariant to compare with target
    
    
    Returns
    -------
    [lower, upper] : list

    lower : conjecture object
           - 'If G satisfies hyp, then target(G) >= m*invariant(G)' 
            where m = min{target(G)/invariant(G): G is in the graph database}

    upper : conjecture object      
           - 'If G satisfies hyp, then target(G) <= M*invariant(G)',
            where M = max{target(G)/invariant(G): G is in the graph database}.

    """

    
    ratios = [] 

    for G in graphs:
        ratios.append(Fraction(G[target] / G[invariant]).limit_denominator(1000))
    
    if ratios == []:
        lower = None
        upper = None
        return lower, upper
    
    else:
        ratios.sort()
        m = min(ratios)
        M = max(ratios)

        if m == 1:
            lower = Conjecture(hyp, target, " >= ", f"{invariant}")
        elif m > -4 and m < 4:
            lower = Conjecture(hyp, target, " >= ", f"{m} * {invariant}")
        else:
            lower = None

        if M == 1:
            upper = Conjecture(hyp, target, " <= ", f"{invariant}")
        elif M > -4 and M < 4:
            upper = Conjecture(hyp, target, " <= ", f"{M} * {invariant}")
        else:
            upper = None
        
        return [lower, upper]


def make_constant(graphs, hyp, target, invariant):
    """
    Parameters
    ----------
    graphs : dictionary of graphs with precomputed graph properties

    hyp : hypothesis object

    target : graph invariant to conjecture on

    invariant : graph invariant to compare with target

    
    
    Returns
    -------
    [lower, upper] : list
          
    lower : conjecture object
           - 'If G satisfies hyp, then target(G) >= invariant(G) + m' 
            where m = min{target(G) - invariant(G): G is in the graph database}

    upper : conjecture object      
           - 'If G satisfies hyp, then target(G) <= invariant(G) + M',
            where M = max{target(G) - invariant(G): G is in the graph database}.

    """

    constants = []

    for G in graphs:
        constants.append(G[target] - G[invariant])

    if constants == []:
        lower = None
        upper = None
        return lower, upper

    else:
        constants.sort()
        m = min(constants)
        M = max(constants)

        if m == 0:
            lower = Conjecture(hyp, target, " >= ", f"{invariant}")
        elif m > -4 and m < 4:
            lower = Conjecture(hyp, target, " >= ", f"{invariant} + {m}")
        else:
            lower = None

        if M == 0:
            upper = Conjecture(hyp, target, " <= ", f"{invariant}")
        elif M > -4 and M < 4:
            upper = Conjecture(hyp, target, " <= ", f"{invariant} + {M}")
        else:
            upper = None

        return [lower, upper]


def make_constant_two(graphs, hyp, target, invariant1, invariant2):
    """
    Parameters
    ----------
    graphs : dictionary of graphs with precomputed graph properties

    hyp : hypothesis object

    target : graph invariant to conjecture on

    invariant1 : graph invariant to compare with target

    invariant2 : graph invariant to compare with target
    
    
    Returns
    -------
    [lower, upper] : list
          
    lower : conjecture object 
            - 'If G satisfies hyp, then target(G) >= invariant1(G)/invariant2(G) + m' 
            where m = min{target(G) - invariant1(G)/invariant2(G): G is in the graph database}
          
    upper : conjecture object
            - 'If G satisfies hyp, then target(G) <= invariant1(G)/invariant2(G) + M',
            where M = min{target(G) - invariant1(G)/invariant2(G): G is in the graph database}.

    """
    constants = []
    

    for G in graphs:
        constants.append(Fraction(G[target] - (G[invariant1] / G[invariant2])).limit_denominator(1000))
    if constants == []:
        upper = None
        lower = None
        return lower, upper
    else:
        m = min(constants)
        M = max(constants)

        if m == 0:
            lower  = Conjecture(hyp, target, " >= ", f"{invariant1} / {invariant2}")
        elif m > -4 and m < 4:
            lower = Conjecture(hyp, target, " >= ", f"( {invariant1} / {invariant2} ) + {m}")
        else:
            lower = None

        if M == 0:
            upper  = Conjecture(hyp, target, " <= ", f"{invariant1} / {invariant2}")
        elif M > -4 and M < 4:
            upper = Conjecture(hyp, target, " <= ", f"( {invariant1} / {invariant2} ) + {M}")
        else:
             upper = None
                            
        return lower, upper 


def make_ratio_two(graphs, hyp, target, invariant1, invariant2):
    """
    Parameters
    ----------
    graphs : dictionary of graphs with precomputed graph properties

    hyp : hypothesis object

    target : graph invariant to conjecture on

    invariant1 : graph invariant to compare with target

    invariant2 : graph invariant to compare with target
    
    
    Returns
    -------
    [lower, upper] : list
          
    lower : conjecture object 
            - 'If G satisfies hyp, then target(G) >= m*(invariant1(G) + invariant2(G))' 
             where m = min{target(G)/ (invariant1(G) + invariant2(G)): G is in the graph database}
          
    upper : conjecture object 
            - 'If G satisfies hyp, then target(G) <= M*(invariant1(G) + invariant2(G))' 
             where M = max{target(G)/ (invariant1(G) + invariant2(G)): G is in the graph database}

    """

    ratios = []

    for G in graphs:
        ratios.append(Fraction(G[target] / (G[invariant1] + G[invariant2])).limit_denominator(1000))
    
    if ratios == []:
        upper = None
        lower = None
        return lower, upper
    
    else:
        m = min(ratios)
        M = max(ratios)

        if m == 1:
            lower = Conjecture(hyp, target, " >= ", f"{invariant1} + {invariant2}")
        elif m > -4 and m < 4:
            lower = Conjecture(hyp, target, " >= ", f"{m} * ( {invariant1} + {invariant2} )")
        else: 
            lower = None

        if M == 1:
            upper = Conjecture(hyp, target, " <= ", f"{invariant1} + {invariant2}")
        elif M > -4 and M < 4:
            upper = Conjecture(hyp, target, " <= ", f"{M} * ( {invariant1} + {invariant2} )")
        else: 
            upper = None

        return [lower, upper]
        


def make_ratio_three(graphs, hyp, target, invariant1, invariant2):
    """
    Parameters
    ----------
    graphs : dictionary of graphs with precomputed graph properties

    hyp : hypothesis object

    target : graph invariant to conjecture on

    invariant1 : graph invariant to compare with target

    invariant2 : graph invariant to compare with target
    
    
    Returns
    -------
    [lower, upper] : list
          
    lower : conjecture object 
            - 'If G satisfies hyp, then target(G) >= m*(invariant2(G)/invariant1(G))' 
             where m = min{target(G)*(invariant1(G)/invariant2(G)): G is in the graph database}
          
    upper : conjecture object 
            - 'If G satisfies hyp, then target(G) <= M*(invariant2(G)/invariant1(G))' 
             where M = max{target(G)/ (invariant1(G) + invariant2(G)): G is in the graph database}

    """
    ratios = []

    for G in graphs:
        ratios.append(Fraction((G[target] * (G[invariant1]) / G[invariant2])).limit_denominator(1000))

    if ratios == []:
        upper = None
        lower = None
        return [lower, upper]

    else:
        m = min(ratios)
        M = max(ratios)

        if m == 1:
            lower = Conjecture(hyp, target, " >= ", f"{invariant2} / {invariant1}")
        elif m > -4 and m < 4:
            lower = Conjecture(hyp, target, " >= ", f"{m} * ( {invariant2} / {invariant1} )")
        else:
            lower = None
    
        if M == 1:
            upper = Conjecture(hyp, target, " <= ", f"{invariant2} / {invariant1}")
        elif M > -4 and M < 4:
            upper = Conjecture(hyp, target, " <= ", f"{M} * ( {invariant2} / {invariant1} )")
        else:
            upper = None

        return [lower, upper]




def make_ratio_four(graphs, hyp, target, invariant1, invariant2):
    """
    Parameters
    ----------
    graphs : dictionary of graphs with precomputed graph properties

    hyp : hypothesis object

    target : graph invariant to conjecture on

    invariant1 : graph invariant to compare with target

    invariant2 : graph invariant to compare with target
    
    
    Returns
    -------
    [lower, upper] : list
          
    lower : conjecture object 
            - 'If G satisfies hyp, then target(G) >= m*(invariant1(G) - invariant2(G))' 
             where m = min{target(G)/ (invariant1(G) - invariant2(G)): G is in the graph database}
          
    upper : conjecture object 
            - 'If G satisfies hyp, then target(G) <= M*(invariant1(G) - invariant2(G))' 
             where M = max{target(G)/ (invariant1(G) - invariant2(G)): G is in the graph database}

    """

    ratios = []
    for G in graphs:
        if G[invariant1] != G[invariant2]:
            ratios.append(Fraction(G[target] / (G[invariant1] - G[invariant2])).limit_denominator(1000))

    if ratios == []:
        upper = None
        lower = None
        return lower, upper
    
    else:
        m = min(ratios)
        M = max(ratios)

        if m == 1:
            lower = Conjecture(hyp, target, " >= ", f"{invariant1} - {invariant2}")
        elif m > -4 and m < 4:
            lower = Conjecture(hyp, target, " >= ", f"{m} * ( {invariant1} - {invariant2} )")
        else: 
            lower = None

        if M == 1:
            upper = Conjecture(hyp, target, " <= ", f"{invariant1} - {invariant2}")
        elif M > -4 and M < 4:
            upper = Conjecture(hyp, target, " <= ", f"{M} * ( {invariant1} - {invariant2} )")
        else: 
            upper = None

        return [lower, upper]





############### These functions are currently not finished/ used in making the conjecture data base ##############

def make_ratio_five(graphs, hyp, target, invariant1, invariant2, invariant3):
    
    ratios = []


    for G in graphs:
        if G[invariant1] != G[invariant2]:
            ratios.append(Fraction((G[target] * (G[invariant1]) / (G[invariant2] + G[invariant3]))).limit_denominator(1000))

    if ratios == []:
        upper = None
        lower = None
        return lower, upper
    
    else:
        m = min(ratios)
        M = max(ratios)
    
        if m == 1:
            upper = Conjecture(hyp, target, " <= ", f"( {invariant2} + {invariant3} ) / {invariant1}")
        elif m > -4 and m < 4:
            upper = Conjecture(hyp, target, " <= ", f"{m} * ( {invariant2} + {invariant3} ) / {invariant1} ")
        else:
            upper = None

        if M == 1:
            upper = Conjecture(hyp, target, " <= ", f"( {invariant2} + {invariant3} ) / {invariant1}")
        elif M > -4 and M < 4:
            upper = Conjecture(hyp, target, " <= ", f"{M} * ( {invariant2} + {invariant3} ) / {invariant1} ")
        else:
            upper = None
        
        return [lower, upper]



