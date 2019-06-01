import itertools
import multiprocessing
import pathlib
import pickle

import grinpy as gp

from tnp.invariants import invariants
from tnp.properties import properties


__all__ = ["make_graph_db"]


def _read_graph_files():
    graph_dir = pathlib.Path("tnp/graph_data/small_connected")
    for path in graph_dir.iterdir():
        if path.is_file():
            yield path.name, gp.read_edgelist(path)


def _calculate(graph_name, graph):
    return graph_name, {f.name: f(graph) for f in itertools.chain(invariants, properties)}


def make_graph_db():
    graphs = _read_graph_files()
    graph_calculations = {}

    with multiprocessing.Pool() as pool:
        for name, calculations in pool.starmap(_calculate, graphs):
            graph_calculations[name] = calculations

    with open("tnp/graph_data/small_simple_graphs_db_2", "wb") as outfile:
        pickle.dump(graph_calculations, outfile)
