from classes.conjecture_class import conjecture
from classes.conclusion_class import conclusion
from classes.hypothesis_class import hypothesis



def check_conjecture(conj, graphs):
    for G in graphs:
        if conj(G.Graph) == False:
            return False
    return True

def hypothesis_true_graphs(conj, graphs):
    return [G.name for G in graphs if conj.hypothesis(G.Graph) == True]
   
def sharp_graphs(conj, graphs):
    return [G.name for G in graphs if conj.conclusion.check_sharp(G.Graph) == True]

def touch_number(conj, graphs):
    return len(sharp_graphs(conj, graphs))

def dalmation_check(conj, known_conjectures):
    for known_conj  in known_conjectures:
        if list(set(hypothesis_true_graphs(conj) - set(hypothesis_true_graphs(known_conj)))) == []:
            return False
    return True

def touch_check(conj, graphs, k = 1):
    return touch_number(conj, graphs) > k




        




    

