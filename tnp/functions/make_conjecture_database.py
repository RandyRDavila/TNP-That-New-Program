import itertools
import pickle

from tnp.functions.Theo import Theo
from main import make_conjectures_one, make_conjectures_two, make_conjectures_three, make_conjectures_four


def make_conjs(target):
    L1 = (c for c in make_conjectures_one(target) if c)
    L2 = (c for c in make_conjectures_two(target) if c)
    L3 = (c for c in make_conjectures_three(target) if c)
    L4 = (c for c in make_conjectures_four(target) if c)

    upper_bounds = (c for c in itertools.chain(L1, L2, L3, L4) if c.inequality == " <= ")
    lower_bounds = (c for c in itertools.chain(L1, L2, L3, L4) if c.inequality == " >= ")

    return Theo(upper_bounds), Theo(lower_bounds)


def conjecture_db(target):
    U, L = make_conjs(target)
    conj_dict = {"upper": U, "lower": L}
    pickle_out = open(f"tnp/graph_data/{target}_conjectures", "wb")
    pickle.dump(conj_dict, pickle_out)
    pickle_out.close()
    return None
