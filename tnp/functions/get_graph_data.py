# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: Randy Davila <davilar@uhd.edu>
"""Function for reading in the conjecture data.
"""
import pickle

__all__ = ["get_graph_data"]


def get_graph_data():
    """Returns current stored conjectures on graph invariant target.
    Parameters
    ----------
    target :   string
               A graph invariant computable by grinpy.

    family :   string
               A name of a given graph family stored in TxGraffiti.
    Returns
    -------
    db :   dictionary
           The dictionary with key values equal to conjectured inequalities
           and whose values are associated with a given conjecture.
    """
    with open(f"tnp/graph_data/small_simple_graphs_db", "rb") as pickle_file:
        db = pickle.load(pickle_file)
    return db
