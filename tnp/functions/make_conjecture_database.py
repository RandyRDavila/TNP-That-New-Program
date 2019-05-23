import pickle

from tnp.functions.Theo import Theo
from main import make_conjectures_one, make_conjectures_two, make_conjectures_three, make_conjectures_four


def make_conjs(target):
    U = []
    L = []

    L1 = list(filter(None, make_conjectures_one(target)))
    L2 = list(filter(None, make_conjectures_two(target)))
    L3 = list(filter(None, make_conjectures_three(target)))
    L4 = list(filter(None, make_conjectures_four(target)))
    for x in L1:
        if x.inequality == " <= ":
            U.append(x)
        else:
            L.append(x)
    for x in L2:
        if x.inequality == " <= ":
            U.append(x)
        else:
            L.append(x)

    for x in L3:
        if x.inequality == " <= ":
            U.append(x)
        else:
            L.append(x)

    for x in L4:
        if x.inequality == " <= ":
            U.append(x)
        else:
            L.append(x)

    return Theo(U), Theo(L)


def conjecture_db(target):
    U, L = make_conjs(target)
    conj_dict = {"upper": U, "lower": L}
    pickle_out = open(f"tnp/graph_data/{target}_conjectures", "wb")
    pickle.dump(conj_dict, pickle_out)
    pickle_out.close()
    return None
