from tnp.graph_data.functions.graph_calculator import calc, graph_property_check
from tnp.graph_data.functions.graph_property_names import invariant_names, property_names
import grinpy as gp
import os
import pickle


__all__ = ["make_graph_db"]


def make_graph_db():

    graphs = [line[:-1] for line in os.popen("ls " + "tnp/graph_data/small_connected")]

    pickle_dict = dict()
    for graph in graphs:

        pickle_dict[graph] = dict()

        G = gp.read_edgelist("tnp/graph_data/small_connected/" + graph)

        for name in invariant_names:
            pickle_dict[graph][name] = calc(G, name)
        for name in property_names:
            pickle_dict[graph][name] = graph_property_check(G, name)

    pickle_out = open("tnp/graph_data/small_simple_graphs_db", "wb")
    pickle.dump(pickle_dict, pickle_out)
    pickle_out.close()

    return None
