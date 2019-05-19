# -*- coding: utf-8 -*-

#    Copyright (C) 2018 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Function for computing the triameter of a graph. 
"""

from itertools import combinations
import grinpy as gp



__all__=['triameter']


def triameter(G):
    """Returns the triameter of the graph G with at least 3 nodes.
    The *triameter* of a graph G with vertex set *V* is defined as the
    following maximum value
    .. math::
        \max\{d(v,w) + d(w,z) + d(v,z): v,w,z \in V: \} 
    
    ----------
    G : NetworkX graph
        An undirected graph with order at least 3.
    -------
    Int:
        The triameter of the graph G.
   
    Examples
    --------
    >>> G = nx.cycle_graph(5)
    >>> nx.triameter(G)
    True
    References
    ----------
    
    A. Das, The triameter of graphs, ArXiv preprint arXiv:1804.01088, 2018.
    https://arxiv.org/pdf/1804.01088.pdf
    """
    d = []
    for s in combinations(G.nodes(), 3):
        s = list(s)
        x1 = len(gp.shortest_path(G,source=s[0],target=s[1]))
        x2 = len(gp.shortest_path(G,source=s[1],target=s[2]))
        x3 = len(gp.shortest_path(G,source=s[0],target=s[2]))
        d.append(x1+x2+x3)
    
    return max(d)









