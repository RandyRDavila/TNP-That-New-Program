import itertools
import json
import multiprocessing
import pathlib

import grinpy as gp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tnp.db.models import Base, Graph
from tnp.invariants import invariants
from tnp.properties import properties


def _calculate_invariants_and_properties(graph):
    return graph, {func.name: func(graph) for func in itertools.chain(invariants, properties)}


def _make_graph_table(db_session, datafile=None):
    # TODO: Allow reading datafile name from config file
    if datafile is None:
        datafile = "graphs.json"

    # Read the datafile and generate NetworkX graphs from the node-link data
    json_ = pathlib.Path(datafile).read_text()
    nx_graphs = (gp.node_link_graph(node_link_data) for node_link_data in json.loads(json_))

    # Calculate all graph invariant and property values for the graphs
    # and add the results to the database
    with multiprocessing.Pool() as pool:
        for nx_graph, calculations in pool.imap(_calculate_invariants_and_properties, nx_graphs):
            db_graph = Graph(json=json.dumps(gp.node_link_data(nx_graph)), **calculations)
            db_session.add(db_graph)

    db_session.commit()


def generate_database(graph_datafile=None):
    # Create the database
    engine = create_engine("sqlite:///tnp.db")
    Base.metadata.create_all(engine)

    # Set-up the datbase session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Make the database tables
    _make_graph_table(session, datafile=graph_datafile)


if __name__ == "__main__":
    generate_database(graph_datafile="data/small_connected_graphs.json")
