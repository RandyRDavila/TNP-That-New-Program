import networkx as nx
import grinpy as gp
from TxGraffiti.graph_data.functions.triameter import triameter
from TxGraffiti.graph_data.functions.domination import domination_number, total_domination_number
from TxGraffiti.graph_data.functions.domination import independent_domination_number
from TxGraffiti.graph_data.functions.chromatic_number import chromatic_number
from TxGraffiti.graph_data.functions.matching_number import matching_number
from TxGraffiti.graph_data.functions.vertex_cover_number import vertex_cover_number
from TxGraffiti.graph_data.functions.independence_number import independence_number
from TxGraffiti.graph_data.functions.topological_indicies import *

__all__ = ["calc", "graph_property_check"]


def calc(G, invariant):
    if invariant == "domination_number":
        return gp.domination_number(G)
    elif invariant == "chromatic_number":
        return gp.chromatic_number(G)
    elif invariant == "total_domination_number":
        return gp.total_domination_number(G)
    elif invariant == "connected_domination_number":
        return gp.connected_domination_number(G)
    elif invariant == "independent_domination_number":
        return gp.independent_domination_number(G)
    elif invariant == "slater":
        return gp.slater(G)
    elif invariant == "sub_total_domination_number":
        return gp.sub_total_domination_number(G)
    elif invariant == "annihilation_number":
        return gp.annihilation_number(G)
    elif invariant == "independence_number":
        return gp.independence_number(G)
    elif invariant == "power_domination_number":
        return gp.power_domination_number(G)
    elif invariant == "residue":
        return gp.residue(G)
    elif invariant == "k_residual_index":
        return gp.k_residual_index(G)
    elif invariant == "connected_zero_forcing_number":
        return gp.connected_zero_forcing_number(G)
    elif invariant == "total_zero_forcing_number":
        return gp.total_zero_forcing_number(G)
    elif invariant == "zero_forcing_number":
        return gp.zero_forcing_number(G)
    elif invariant == "diameter":
        return gp.diameter(G)
    elif invariant == "radius":
        return gp.radius(G)
    elif invariant == "order":
        return gp.number_of_nodes(G)
    elif invariant == "size":
        return gp.number_of_edges(G)
    elif invariant == "min_degree":
        return gp.min_degree(G)
    elif invariant == "max_degree":
        return gp.max_degree(G)
    elif invariant == "number_of_min_degree_nodes":
        return gp.number_of_min_degree_nodes(G)
    elif invariant == "number_of_degree_one_nodes":
        return gp.number_of_degree_one_nodes(G)
    elif invariant == "number_of_max_degree_nodes":
        return gp.number_of_max_degree_nodes(G)
    elif invariant == "clique_number":
        return gp.clique_number(G)
    elif invariant == "min_maximal_matching_number":
        return gp.min_maximal_matching_number(G)
    elif invariant == "matching_number":
        return gp.matching_number(G)
    elif invariant == "triameter":
        return gp.triameter(G)
    elif invariant == "vertex_cover_number":
        return gp.vertex_cover_number(G)
    elif invariant == "randic_index":
        return gp.randic_index(G)
    elif invariant == "augmented_randic_index":
        return gp.augmented_randic_index(G)
    elif invariant == "harmonic_index":
        return gp.harmonic_index(G)
    elif invariant == "atom_bond_connectivity_index":
        return gp.atom_bond_connectivity_index(G)
    elif invariant == "sum_connectivity_index":
        return gp.sum_connectivity_index(G)
    else:
        print("ERROR")
        return False


def graph_property_check(G, property):
    if property == "is_bipartite":
        return gp.is_bipartite(G)
    elif property == "is_chordal":
        return gp.is_chordal(G)
    elif property == "has_bridges":
        return gp.has_bridges(G)
    elif property == "is_connected":
        return gp.is_connected(G)
    elif property == "is_distance_regular":
        return gp.is_distance_regular(G)
    elif property == "is_strongly_regular":
        return gp.is_strongly_regular(G)
    elif property == "is_eulerian":
        return gp.is_eulerian(G)
    elif property == "is_planar":
        return gp.check_planarity(G)[0]
    elif property == "is_regular":
        return gp.min_degree(G) == gp.max_degree(G)
    elif property == "is_cubic":
        return gp.min_degree(G) == 3 and gp.max_degree(G) == 3
    elif property == "is_not_K_n":
        return gp.is_isomorphic(G, gp.complete_graph(gp.number_of_nodes(G))) == False
    elif property == "is_triangle_free":
        return set(gp.triangles(G).values()) == {0}
