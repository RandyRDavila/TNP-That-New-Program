# -*- coding: utf-8 -*-

#    Copyright (C) 2018 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing the computing topological indicies of a graph. Many
   of these indicies were developed in relation to chemical graph theory, and 
   some have been related to quantum theory.
"""

import math
from grinpy import neighborhood

__all__ = ['randic_index',
           'augmented_randic_index',
           'harmonic_index',
           'atom_bond_connectivity_index',
           'sum_connectivity_index'
           ]


def degree(G,x):
    return len(neighborhood(G,x))


def randic_index(G):
    """Returns the Randic Index of the graph G.
    The *Randic index* of a graph G with edge set *E* is defined as the
    following sum
    .. math::
        \sum_{vw \in E} \frac{1}{\sqrt(d_G(v)*d_G(w))}
    
    ----------
    G : NetworkX graph
        An undirected graph.
    -------
    float
        The Randic Index of a graph.
   
    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> nx.randic_index(G)
    True
    References
    ----------
    
    Ivan Gutman, Degree-Based Topological Indices† ,Croat. Chem. Acta 86 (4)
    (2013) 351–361.
    http://dx.doi.org/10.5562/cca2294
    """
    f = lambda x, y: 1/ math.sqrt(degree(G,x)*degree(G,y))
    
    return sum([f(e[0],e[1]) for e in list(G.edges())])


def augmented_randic_index(G):
    """Returns the augmented-Randic Index of the graph G.
    The *augmented-Randic index* of a graph G with edge set *E* is defined as the
    following sum
    .. math::
        \sum_{vw \in E} \frac{1}{\max(d_G(v), d_G(w))}
    
    ----------
    G : NetworkX graph
        An undirected graph.
    -------
    float
        The augmented-Randic index of a graph.
   
    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> nx.augmented_randic_index(G)
    True
    References
    ----------
    
    Ivan Gutman, Degree-Based Topological Indices† ,Croat. Chem. Acta 86 (4)
    (2013) 351–361.
    http://dx.doi.org/10.5562/cca2294
    """
    f = lambda x, y: max(degree(G,x),degree(G,y))
    
    return sum([1 / f(e[0],e[1]) for e in list(G.edges())])


def harmonic_index(G):
    """Returns the Harmonic Index of the graph G. This invariant was originally
    introduced by Siemion Fajtlowicz.
    The *harmonic index* of a graph G with edge set *E* is defined as the
    following sum
    .. math::
        \sum_{vw \in E} \frac{1}{d_G(v) + d_G(w)}
    
    ----------
    G : NetworkX graph
        An undirected graph.
    -------
    float
        The harmonic index of a graph.
   
    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> nx.harmonic_index(G)
    True
    References
    ----------
    
    Ivan Gutman, Degree-Based Topological Indices† ,Croat. Chem. Acta 86 (4)
    (2013) 351–361.
    http://dx.doi.org/10.5562/cca2294
    """
    f = lambda x, y: degree(G,x) + degree(G,y)
    
    return sum([2/f(e[0], e[1]) for e in list(G.edges())])
   

def atom_bond_connectivity_index(G):
    """Returns the atom bond connectivity Index of the graph G.
    The *atom bond connectivity index* of a graph G with edge set *E* is defined as the
    following sum
    .. math::
        \sum_{vw \in E} \sqrt(\frac{d_G(v) + d_G(w) - 2)}{(d_G(v)*d_G(w))}}
    
    ----------
    G : NetworkX graph
        An undirected graph.
    -------
    float
        The atom bond connectivity index of a graph.
   
    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> nx.atom_bond_connectivity_index(G)
    True
    References
    ----------
    
    Ivan Gutman, Degree-Based Topological Indices† ,Croat. Chem. Acta 86 (4)
    (2013) 351–361.
    http://dx.doi.org/10.5562/cca2294
    """
    f = lambda x,y: math.sqrt((degree(G,x) + degree(G,y) - 2)/ (degree(G,x)*degree(G,y)))
    
    return sum([f(e[0],e[1]) for e in list(G.edges())])

def sum_connectivity_index(G):
    """Returns the sum connectivity Index of the graph G.
    The *sum connectivity index* of a graph G with edge set *E* is defined as the
    following sum
    .. math::
        \sum_{vw \in E} \frac{1}{\sqrt(d_G(v) + d_G(w))}
    
    ----------
    G : NetworkX graph
        An undirected graph.
    -------
    float
        The sum connectivity index of a graph.
   
    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> nx.sum_connectivity_index(G)
    True
    References
    ----------
    
    Ivan Gutman, Degree-Based Topological Indices† ,Croat. Chem. Acta 86 (4)
    (2013) 351–361.
    http://dx.doi.org/10.5562/cca2294
    """
    f = lambda x,y: 1/math.sqrt((degree(G,x) + degree(G,y)))
    
    return sum([f(e[0],e[1]) for e in list(G.edges())])


    
    
    

