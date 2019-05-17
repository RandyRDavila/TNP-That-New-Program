from functions.make_expressions import *
from itertools import combinations
from graph_data.functions.graph_property_names import *
from functions.Theo import Theo
from functions.make_hypothesis import *



def make_conjectures(target):
    hyp = make_hypothesis()
    conjs = []
    for h in hyp:
        for i in invariant_names:
            if i != target:
                conjs.append(make_ratio(h, target, i, 'upper'))
                conjs.append(make_ratio(h, target, i, 'lower'))
                conjs.append(make_constant(h, target, i, 'upper'))
                conjs.append(make_constant(h, target, i, 'lower'))

    C = Theo(conjs)
    return C
    
      
def make_conjectures_two(target):
    hyp = make_hypothesis()
    conjs = []
    for h in hyp:
        for i in invariant_names:
            if i != target:
                for i2 in invariant_names:
                    if i2 != i and i2 != target:
                        conjs.append(make_ratios_two(h, target, i, i2, 'upper'))
                        conjs.append(make_ratios_two(h, target, i, i2, 'lower'))

    C = Theo(conjs)
    return C
                        

            

