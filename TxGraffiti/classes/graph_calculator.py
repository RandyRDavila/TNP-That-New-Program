import grinpy as GPY
import networkx as nx


def calc(G, invariant):
    if invariant == "domination_number":
        return GPY.domination_number(G)
    elif invariant == "chromatic_number":
        return GPY.chromatic_number(G)
    elif invariant == "total_domination_number":
        return GPY.total_domination_number(G)
    elif invariant == "connected_domination_number":
        return GPY.connected_domination_number(G)
    elif invariant == "independent_domination_number":
        return GPY.independent_domination_number(G)
    elif invariant == "slater":
        return GPY.slater(G)
    elif invariant == "sub_total_domination_number":
        return GPY.sub_total_domination_number(G)
    elif invariant == "annihilation_number":
        return GPY.annihilation_number(G)
    elif invariant == "independence_number":
        return GPY.independence_number(G)
    elif invariant == "power_domination_number":
        return GPY.power_domination_number(G)
    elif invariant == "residue":
        return GPY.residue(G)
    elif invariant == "k_residual_index":
        return GPY.k_residual_index(G)
    elif invariant == "connected_zero_forcing_number":
        return GPY.connected_zero_forcing_number(G)
    elif invariant == "total_zero_forcing_number":
        return GPY.total_zero_forcing_number(G)
    elif invariant == "zero_forcing_number":
        return GPY.zero_forcing_number(G)
    elif invariant == "diameter":
        return nx.diameter(G)
    elif invariant == "radius":
        return nx.radius(G)
    elif invariant == "order":
        return nx.number_of_nodes(G)
    elif invariant == "size":
        return nx.number_of_edges(G)
    elif invariant == "min_degree":
        return GPY.min_degree(G)
    elif invariant == "max_degree":
        return GPY.max_degree(G)
    elif invariant == "number_of_min_degree_nodes":
        return GPY.number_of_min_degree_nodes(G)
    elif invariant == "number_of_degree_one_nodes":
        return GPY.number_of_degree_one_nodes(G)
    elif invariant == "number_of_max_degree_nodes":
        return GPY.number_of_max_degree_nodes(G)
    elif invariant == "clique_number":
        return GPY.clique_number(G)
    elif invariant == "min_maximal_matching_number":
        return GPY.min_maximal_matching_number(G)
    elif invariant == "matching_number":
        return GPY.matching_number(G)

    else:
        print("ERROR")
        return False
