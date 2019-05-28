import grinpy as gp

from tnp._base_classes import _GraphCallable, _NamespaceIterator
from tnp.graph_data.functions.triameter import triameter
from tnp.graph_data.functions.topological_indicies import (
    atom_bond_connectivity_index,
    augmented_randic_index,
    harmonic_index,
    randic_index,
    sum_connectivity_index,
)


class Invariant(_GraphCallable):
    pass


class _invariants(_NamespaceIterator):
    type = Invariant

    class namespace:
        domination_number = Invariant(function=gp.domination_number)
        total_domination_number = Invariant(function=gp.total_domination_number)
        connected_domination_number = Invariant(function=gp.connected_domination_number)
        independence_number = Invariant(function=gp.independence_number)
        power_domination_number = Invariant(function=gp.power_domination_number)
        zero_forcing_number = Invariant(function=gp.zero_forcing_number)
        total_zero_forcing_number = Invariant(function=gp.total_zero_forcing_number)
        connected_zero_forcing_number = Invariant(function=gp.connected_zero_forcing_number)
        diameter = Invariant(function=gp.diameter)
        radius = Invariant(function=gp.radius)
        order = Invariant(function=gp.number_of_nodes, name="order")
        size = Invariant(function=gp.number_of_edges, name="size")
        independent_domination_number = Invariant(function=gp.independent_domination_number)
        chromatic_number = Invariant(function=gp.chromatic_number)
        matching_number = Invariant(function=gp.matching_number)
        min_maximal_matching_number = Invariant(function=gp.min_maximal_matching_number)
        triameter = Invariant(function=triameter)  # TODO: Add to GrinPy
        randic_index = Invariant(function=randic_index)  # TODO: Add to GrinPy
        augmented_randic_index = Invariant(function=augmented_randic_index)  # TODO: Add to GrinPy
        harmonic_index = Invariant(function=harmonic_index)  # TODO: Add to GrinPy
        atom_bond_connectivity_index = Invariant(function=atom_bond_connectivity_index)  # TODO: Add to GrinPy
        sum_connectivity_index = Invariant(function=sum_connectivity_index)  # TODO: Add to GrinPy
        min_degree = Invariant(function=gp.min_degree)
        max_degree = Invariant(function=gp.max_degree)
        number_of_min_degree_nodes = Invariant(function=gp.number_of_min_degree_nodes)
        number_of_max_degree_nodes = Invariant(function=gp.number_of_max_degree_nodes)
        clique_number = Invariant(function=gp.clique_number)
        residue = Invariant(function=gp.residue)
        annihilation_number = Invariant(function=gp.annihilation_number)


invariants = _invariants()
