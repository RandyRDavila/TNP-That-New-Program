import pickle

from TxGraffiti.functions.heuristics import Theo
#from main import make_conjectures_one, make_conjectures_two, make_conjectures_three, make_conjectures_four
from TxGraffiti.functions.make_conjectures import make_conjectures

def make_conjs(target):
    U = []
    L = []
    C = make_conjectures(target)
   
    C = list(filter(None, make_conjectures(target)))
    for x in C:
        if x.inequality == ' <= ':
            U.append(x)
        else:
            L.append(x)
    
    return U, L


def conjecture_db(target, regular_exception = False):
    U, L = make_conjs(target)
    conj_dict = {"upper": U, "lower": L}
    pickle_out = open(f"TxGraffiti/conjectures/{target}_conjectures", "wb")
    pickle.dump(conj_dict, pickle_out)
    pickle_out.close()
    return None
