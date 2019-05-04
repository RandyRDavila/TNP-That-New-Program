
# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: Randy Davila <davilar@uhd.edu>
"""Function for reading in the conjecture data.
"""
import pickle

__all__ = ['get_conjectures']


def get_conjectures(target, family):
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
    with open(f'graph_data/{target}_{family}_conjectures', 'rb') as pickle_file:
        db = pickle.load(pickle_file)
    return db

def remove_duplicates(lst):
    res = []
    for x in lst:
        if x not in res:
            res.append(x)
    return res
