from functions.make_expressions import *
from itertools import combinations
from graph_data.functions.graph_property_names import *
from functions.Theo import Theo
from functions.make_hypothesis import *



def make_conjectures_one(target):
    hyp = make_hypothesis(4)
    conjs = []
    for h in hyp:
        for i in invariant_names:
            if i != target:
                conjs.append(make_ratio(h, target, i, 'upper'))
                conjs.append(make_ratio(h, target, i, 'lower'))
                conjs.append(make_constant(h, target, i, 'upper'))
                conjs.append(make_constant(h, target, i, 'lower'))

    #C = Theo(conjs)
    return conjs
    
      
def make_conjectures_two(target):
    hyp = make_hypothesis(3)
    conjs = []
    for h in hyp:
        for c in combinations(invariant_names,2):
            c = list(c)
            if c[1] != c[0] and c[1] != target and c[0] != target:
                conjs.append(make_ratio_two(h, target, c[0], c[1], 'upper'))
                conjs.append(make_ratio_two(h, target, c[0], c[1], 'lower'))

    #C = Theo(conjs)
    return conjs
                        
def make_conjectures_three(target):
    hyp = make_hypothesis(3)
    conjs = []
    for h in hyp:
        for c in combinations(invariant_names,2):
            c = list(c)
            if c[1] != c[0] and c[1] != target and c[0] != target:
                conjs.append(make_ratio_three(h, target, c[0], c[1], 'upper'))
                conjs.append(make_ratio_three(h, target, c[0], c[1], 'lower'))

    C = Theo(conjs)
    return C
            

def make_conjectures_four(target):
    hyp = make_hypothesis(3)
    conjs = []
    for h in hyp:
        for c in combinations(invariant_names,2):
            c = list(c)
            if c[1] != c[0] and c[1] != target and c[0] != target:
                conjs.append(make_constant_two(h, target, c[0], c[1], 'upper'))
                conjs.append(make_constant_two(h, target, c[0], c[1], 'lower'))

    C = Theo(conjs)
    return C