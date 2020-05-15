from TxGraffiti.functions.make_expressions import *
from TxGraffiti.functions.heuristics import Theo, Dalmation, Romy
from TxGraffiti.functions.get_graph_data import get_hypothesis_data
from TxGraffiti.functions.filters import desired_invariant_names
from TxGraffiti.functions.filters import regular_exclusion_invariant_names
from TxGraffiti.functions.get_graph_data import get_graph_data
from TxGraffiti.functions.decorators import timer
from itertools import combinations



__all__ = ['make_conjs']


@timer
def make_conjs(target, 
                two_hypothesis = False, 
                two_invariants = False, 
                data_set = 'test_data',
                use_Dalmation = False,
                use_Romy = False):
    
    conjs = []
    hypothesis = get_hypothesis_data()[1]
    invariant_names = desired_invariant_names(target)
   
    graphs_hold = get_graph_data(data_set)

    for h in hypothesis:
        graphs = graphs_hold.copy()
        graphs = [graphs[G] for G in graphs if h(graphs[G]) is True]
        new_invariant_names = regular_exclusion_invariant_names(h, invariant_names)
        for invar in new_invariant_names:
            
            temp_conjs = list(filter(None, make_ratio(graphs, h, target, invar)))
            for c in temp_conjs:
                conjs.append(c)
            
            temp_conjs = list(filter(None, make_constant(graphs,h, target, invar)))
            for c in temp_conjs:
                conjs.append(c)

        if two_invariants == True:
            for invars in combinations(new_invariant_names,2):
                invars = list(invars)

                temp_conjs = list(filter(None, make_constant_two(graphs, h, target, invars[0], invars[1])))
                for c in temp_conjs:
                    conjs.append(c)

                temp_conjs = list(filter(None, make_constant_two(graphs, h, target, invars[1], invars[0])))
                for c in temp_conjs:
                    conjs.append(c)

                temp_conjs = list(filter(None, make_ratio_two(graphs, h, target, invars[0], invars[1])))
                for c in temp_conjs:
                    conjs.append(c)

                temp_conjs = list(filter(None, make_ratio_three(graphs, h, target, invars[0], invars[1])))
                for c in temp_conjs:
                    conjs.append(c)
                
                temp_conjs = list(filter(None, make_ratio_three(graphs, h, target, invars[1], invars[0])))
                for c in temp_conjs:
                    conjs.append(c)

    if two_hypothesis == True:
        hypothesis = get_hypothesis_data()[2]

        for h in hypothesis:
            graphs = graphs_hold.copy()
            graphs = [graphs[G] for G in graphs if h(graphs[G]) is True]
            new_invariant_names = regular_exclusion_invariant_names(h, invariant_names)
            for invar in new_invariant_names:
            
                temp_conjs = list(filter(None, make_ratio(graphs, h, target, invar)))
                for c in temp_conjs:
                    conjs.append(c)
            
                temp_conjs = list(filter(None, make_constant(graphs, h, target, invar)))
                for c in temp_conjs:
                    conjs.append(c)

            if two_invariants == True:
                for invars in combinations(new_invariant_names,2):
                    invars = list(invars)

                    temp_conjs = list(filter(None, make_constant_two(graphs, h, target, invars[0], invars[1])))
                    for c in temp_conjs:
                        conjs.append(c)

                    temp_conjs = list(filter(None, make_constant_two(graphs, h, target, invars[1], invars[0])))
                    for c in temp_conjs:
                        conjs.append(c)

                    temp_conjs = list(filter(None, make_ratio_two(graphs, h, target, invars[0], invars[1])))
                    for c in temp_conjs:
                        conjs.append(c)

                    temp_conjs = list(filter(None, make_ratio_three(graphs, h, target, invars[0], invars[1])))
                    for c in temp_conjs:
                        conjs.append(c)
                
                    temp_conjs = list(filter(None, make_ratio_three(graphs, h, target, invars[1], invars[0])))
                    for c in temp_conjs:
                        conjs.append(c)

    if use_Dalmation == True:
        return Dalmation(Theo(conjs))
    elif use_Romy == True:
        return Romy(Theo(conjs))
    else:
        return Theo(conjs)



