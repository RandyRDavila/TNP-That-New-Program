import os
import pickle

import grinpy as gp

from TxGraffiti.graph_data.functions.graph_calculator import calc, graph_property_check
from TxGraffiti.graph_data.functions.graph_property_names import invariant_names, property_names


__all__ = ["make_graph_db", "make_graph6_db"]


def make_graph_db():

    graphs = [line[:-1] for line in os.popen("ls " + "TxGraffiti/graph_data/small_connected")]

    pickle_dict = dict()
    for graph in graphs:

        pickle_dict[graph] = dict()

        G = gp.read_edgelist("TxGraffiti/graph_data/small_connected/" + graph)

        for name in invariant_names:
            pickle_dict[graph][name] = calc(G, name)
        for name in property_names:
            pickle_dict[graph][name] = graph_property_check(G, name)

    pickle_out = open("TxGraffiti/graph_data/small_simple_graphs_db", "wb")
    pickle.dump(pickle_dict, pickle_out)
    pickle_out.close()

    return None



def make_graph6_db(order, family = 'graph'):

    graphs = gp.read_graph6(f'TxGraffiti/graph6_data/{family}{order}c.g6')
   
    
    pickle_dict = dict()
    i = 0
    for graph in graphs:
        pickle_dict[f'{family}-{order}-graph{i}'] = dict()

        for name in invariant_names:
            pickle_dict[f'{family}-{order}-graph{i}'][name] = calc(graph, name)
        for name in property_names:
            pickle_dict[f'{family}-{order}-graph{i}'][name] = graph_property_check(graph, name)

        i += 1

    return pickle_dict

