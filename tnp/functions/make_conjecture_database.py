from functions.make_expressions import *
from itertools import combinations
from graph_data.functions.graph_property_names import *
from functions.Theo import Theo
from functions.make_hypothesis import *
import pickle
from main import *


def make_conjs(target):
    U = []
    L = []

    L1 = list(filter(None, make_conjectures_one(target))) 
    L2 = list(filter(None, make_conjectures_two(target))) 
    L3 = list(filter(None, make_conjectures_three(target)))
    L4 = list(filter(None, make_conjectures_four(target)))
    for x in L1:
        if x.inequality == ' <= ':
            U.append(x)
        else:
            L.append(x)
    for x in L2:
        if x.inequality == ' <= ':
            U.append(x)
        else:
            L.append(x)

    for x in L3:
        if x.inequality == ' <= ':
            U.append(x)
        else:
            L.append(x)

    for x in L4:
        if x.inequality == ' <= ':
            U.append(x)
        else:
            L.append(x)

    return Theo(U), Theo(L)


def conjecture_db(target):
    U, L = make_conjs(target)
    conj_dict = {'upper': U, 'lower': L}
    pickle_out = open(f'graph_data/{target}_conjectures', 'wb')
    pickle.dump(conj_dict, pickle_out)
    pickle_out.close()
    return None
