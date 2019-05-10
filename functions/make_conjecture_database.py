from functions.get_graph_data import get_graph_data
from functions.make_conjectures import *
from classes.hypothesis_class import hypothesis
from graph_data.functions.graph_property_names import invariant_names, property_names
from itertools import combinations
import grinpy as gp
import os
import pickle



__all__ = ['make_conjecture_db']

def make_conjecture_db():

    graphs = get_graph_data()

    conjs = []
    for alpha in invariant_names:
        for p in property_names:
            hyp = hypothesis(p)
            for i in invariant_names:
                if i != alpha:
                    conjs.append(make_ratio(hyp, alpha, i, 'upper'))
                    conjs.append(make_ratio(hyp, alpha, i, 'lower'))
                    conjs.append(make_constant(hyp, alpha, i, 'upper'))
                    conjs.append(make_constant(hyp, alpha, i, 'lower'))

    for alpha in invariant_names:
        for h in combinations(property_names, 2):
            h = list(h)
            hyp = hypothesis(h[0], h[1])
            for i in invariant_names:
                if i != alpha:
                    conjs.append(make_ratio(hyp, alpha, i, 'upper'))
                    conjs.append(make_ratio(hyp, alpha, i, 'lower'))
                    conjs.append(make_constant(hyp, alpha, i, 'upper'))
                    conjs.append(make_constant(hyp, alpha, i, 'lower'))

    conjs = [x for x in conjs if x != None]
    conjs.sort(reverse = True, key = lambda c: c.scaled_touch_number())
    
    return conjs

