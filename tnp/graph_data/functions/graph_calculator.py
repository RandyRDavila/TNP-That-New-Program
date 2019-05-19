import networkx as nx
import grinpy as GPY
from tnp.graph_data.functions.triameter import triameter
from tnp.graph_data.functions.domination import domination_number, total_domination_number
from tnp.graph_data.functions.domination import independent_domination_number
from tnp.graph_data.functions.chromatic_number import chromatic_number
from tnp.graph_data.functions.matching_number import matching_number
from tnp.graph_data.functions.vertex_cover_number import vertex_cover_number
from tnp.graph_data.functions.independence_number import independence_number
from tnp.graph_data.functions.topological_indicies import *

__all__ = ['calc', 'graph_property_check']


def calc(G, invariant):
    if invariant == 'domination_number':
        return domination_number(G)
    elif invariant == 'chromatic_number':
        return chromatic_number(G)
    elif invariant == 'total_domination_number':
        return total_domination_number(G)
    elif invariant == 'connected_domination_number':
        return GPY.connected_domination_number(G)
    elif invariant == 'independent_domination_number':
        return independent_domination_number(G)
    elif invariant == 'slater':
        return GPY.slater(G)
    elif invariant == 'sub_total_domination_number':
        return GPY.sub_total_domination_number(G)
    elif invariant == 'annihilation_number':
        return GPY.annihilation_number(G)
    elif invariant == 'independence_number':
        return independence_number(G)
    elif invariant == 'power_domination_number':
        return GPY.power_domination_number(G)
    elif invariant == 'residue':
        return GPY.residue(G)
    elif invariant == 'k_residual_index':
        return GPY.k_residual_index(G)
    elif invariant == 'connected_zero_forcing_number':
        return GPY.connected_zero_forcing_number(G)
    elif invariant == 'total_zero_forcing_number':
        return GPY.total_zero_forcing_number(G)
    elif invariant == 'zero_forcing_number':
        return GPY.zero_forcing_number(G)
    elif invariant == 'diameter':
        return nx.diameter(G)
    elif invariant == 'radius':
        return nx.radius(G)
    elif invariant == 'order':
        return nx.number_of_nodes(G)
    elif invariant == 'size':
        return nx.number_of_edges(G)
    elif invariant == 'min_degree':
        return GPY.min_degree(G)
    elif invariant == 'max_degree':
        return GPY.max_degree(G)
    elif invariant == 'number_of_min_degree_nodes':
        return GPY.number_of_min_degree_nodes(G)
    elif invariant == 'number_of_degree_one_nodes':
        return GPY.number_of_degree_one_nodes(G)
    elif invariant == 'number_of_max_degree_nodes':
        return GPY.number_of_max_degree_nodes(G)
    elif invariant == 'clique_number':
        return GPY.clique_number(G)
    elif invariant == 'min_maximal_matching_number':
        return GPY.min_maximal_matching_number(G)
    elif invariant == 'matching_number':
        return matching_number(G)
    elif invariant == 'triameter':
        return triameter(G)
    elif invariant == 'vertex_cover_number':
        return vertex_cover_number(G)
    elif invariant == 'randic_index':
        return randic_index(G)
    elif invariant == 'augmented_randic_index':
        return augmented_randic_index(G)
    elif invariant == 'harmonic_index':
        return harmonic_index(G)
    elif invariant == 'atom_bond_connectivity_index':
        return atom_bond_connectivity_index(G)
    elif invariant == 'sum_connectivity_index':
        return sum_connectivity_index(G)
    else:
        print('ERROR')
        return False

def graph_property_check(G, property):
    if property == 'is_bipartite':
        return nx.is_bipartite(G)
    elif property == 'is_chordal':
        return nx.is_chordal(G)
    elif property == 'has_bridges':
        return nx.has_bridges(G)
    elif property == 'is_connected':
        return nx.is_connected(G)
    elif property == 'is_distance_regular':
        return nx.is_distance_regular(G)
    elif property == 'is_strongly_regular':
        return nx.is_strongly_regular(G)
    elif property == 'is_eulerian':
        return nx.is_eulerian(G)
    elif property == "is_planar":
        return nx.check_planarity(G)[0]
    elif property == "is_regular":
        return GPY.min_degree(G) == GPY.max_degree(G)
    elif property == "is_cubic":
        return GPY.min_degree(G) == 3 and GPY.max_degree(G) == 3
    elif property == 'is_not_K_n':
        return nx.is_isomorphic(G, nx.complete_graph(nx.number_of_nodes(G))) == False
    elif property == 'is_triangle_free':
        return set(nx.triangles(G).values()) == {0}
