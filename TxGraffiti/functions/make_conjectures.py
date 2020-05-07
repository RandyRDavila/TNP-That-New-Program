from TxGraffiti.functions.make_expressions import *
from itertools import combinations
from TxGraffiti.graph_data.functions.graph_property_names import *
from TxGraffiti.functions.heuristics import Theo, Dalmation
from TxGraffiti.functions.make_hypothesis import *



reg_exception_invariants = ['randic_index',
                                'augmented_randic_index',
                                'harmonic_index', 
                                'atom_bond_connectivity_index',
                                'sum_connectivity_index',]





def make_conjectures(target):
    hyp = make_hypothesis(3, False)

    if target in reg_exception_invariants:
        hyp_temp = []
        for h in hyp:
            if 'is_regular' not in h.properties and 'is_cubic' not in h.properties \
                and 'is_strongly_regular' not in h.properties and 'is_distance_regular' not in h.properties:
                hyp_temp.append(h)
        hyp = hyp_temp

    conjs = []

    if target == 'zero_forcing_number':
        invariant_names.remove('total_zero_forcing_number')
        invariant_names.remove('connected_zero_forcing_number')
        invariant_names.remove('power_domination_number')
    elif target == 'total_zero_forcing_number':
        invariant_names.remove('zero_forcing_number')
        invariant_names.remove('connected_zero_forcing_number')
        invariant_names.remove('power_domination_number')
    elif target == 'connected_zero_forcing_number':
        invariant_names.remove('zero_forcing_number')
        invariant_names.remove('total_zero_forcing_number')
        invariant_names.remove('power_domination_number')
    elif target == 'power_domination_number':
        invariant_names.remove('zero_forcing_number')
        invariant_names.remove('total_zero_forcing_number')
        invariant_names.remove('connected_zero_forcing_number')
    
    invariant_names.remove(target)

    for h in hyp:
        new_invariant_names = invariant_names.copy()
        if 'is_regular' in h.properties or 'is_cubic' in h.properties \
             or 'is_strongly_regular' in h.properties or 'is_distance_regular' in h.properties:
            new_invariant_names.remove('annihilation_number')
            new_invariant_names.remove('max_degree')
            new_invariant_names.remove('number_of_min_degree_nodes')
            new_invariant_names.remove('number_of_max_degree_nodes')
            new_invariant_names.remove('size')
            new_invariant_names.remove('randic_index')
            new_invariant_names.remove('augmented_randic_index')
            new_invariant_names.remove('harmonic_index')
            new_invariant_names.remove('atom_bond_connectivity_index')
            new_invariant_names.remove('sum_connectivity_index')

        for c in new_invariant_names:
            conjs.append(make_ratio(h, target, c, 'upper'))
            conjs.append(make_ratio(h, target, c, 'lower'))
            conjs.append(make_constant(h, target, c, 'upper'))
            conjs.append(make_constant(h, target, c, 'lower'))
        
        for c in combinations(new_invariant_names,2):
            c = list(c)
            conjs.append(make_ratio_two(h, target, c[0], c[1], 'upper'))
            conjs.append(make_ratio_two(h, target, c[0], c[1], 'lower'))
            conjs.append(make_ratio_three(h, target, c[0], c[1], 'upper'))
            conjs.append(make_ratio_three(h, target, c[0], c[1], 'lower'))
        
    
    return Theo(conjs)
