from TxGraffiti.functions.make_conjectures import make_conjs
import pickle


def conjecture_db(target):
    C = make_conjs(target, use_Dalmation = True)
    lower = [x for x in C if x.inequality == ' >= ']
    upper = [x for x in C if x.inequality == ' <= ']
    conj_dict = {"upper": upper, "lower": lower}
    pickle_out = open(f"TxGraffiti/conjectures/{target}_conjectures", "wb")
    pickle.dump(conj_dict, pickle_out)
    pickle_out.close()
    return None
