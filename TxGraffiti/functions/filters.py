


__all__ = ['desired_invariant_names', 
            'regular_exclusion_invariant_names']
            


def desired_invariant_names(target):
    invariant_names = [line.rstrip("\n") 
                        for line 
                        in open("TxGraffiti/graph_data/functions/invariants.txt")
                        ]
    
    if target == 'zero_forcing_number':
        #invariant_names.remove('total_zero_forcing_number')
        #invariant_names.remove('connected_zero_forcing_number')
        invariant_names.remove('power_domination_number')
    #elif target == 'total_zero_forcing_number':
        #invariant_names.remove('zero_forcing_number')
        #invariant_names.remove('connected_zero_forcing_number')
        #invariant_names.remove('power_domination_number')
    #elif target == 'connected_zero_forcing_number':
        #invariant_names.remove('zero_forcing_number')
        #invariant_names.remove('total_zero_forcing_number')
        #invariant_names.remove('power_domination_number')
    elif target == 'power_domination_number':
        invariant_names.remove('zero_forcing_number')
        #invariant_names.remove('total_zero_forcing_number')
        #invariant_names.remove('connected_zero_forcing_number')
    
    invariant_names.remove(target)

    return invariant_names


def regular_exclusion_invariant_names(hyp, invariant_names):
    new_invariant_names = invariant_names.copy()
    if 'is_regular' in hyp.properties or 'is_cubic' in hyp.properties \
        or 'is_strongly_regular' in hyp.properties \
            or 'is_distance_regular' in hyp.properties:
        new_invariant_names.remove('annihilation_number')
        new_invariant_names.remove('max_degree')
        new_invariant_names.remove('number_of_min_degree_nodes')
        new_invariant_names.remove('number_of_max_degree_nodes')
        new_invariant_names.remove('size')
        new_invariant_names.remove('randic_index')
        new_invariant_names.remove('harmonic_index')
        #new_invariant_names.remove('atom_bond_connectivity_index')
        #new_invariant_names.remove('sum_connectivity_index')
    
    return new_invariant_names