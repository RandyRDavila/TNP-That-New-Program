import itertools
import pickle

from tnp.functions.Theo import Theo
from main import make_conjectures_one, make_conjectures_two, make_conjectures_three, make_conjectures_four


def make_conjs(target):
    L11, L12 = itertools.tee((c for c in make_conjectures_one(target) if c), 2)
    L21, L22 = itertools.tee((c for c in make_conjectures_two(target) if c), 2)
    L31, L32 = itertools.tee((c for c in make_conjectures_three(target) if c), 2)
    L41, L42 = itertools.tee((c for c in make_conjectures_four(target) if c), 2)

    upper_bounds = (c for c in itertools.chain(L11, L21, L31, L41) if c.inequality == " <= ")
    lower_bounds = (c for c in itertools.chain(L12, L22, L32, L42) if c.inequality == " >= ")

    return Theo(upper_bounds), Theo(lower_bounds)


def conjecture_db(target):
    U, L = make_conjs(target)
    conj_dict = {"upper": U, "lower": L}
    pickle_out = open(f"tnp/graph_data/{target}_conjectures", "wb")
    pickle.dump(conj_dict, pickle_out)
    pickle_out.close()
    return None
