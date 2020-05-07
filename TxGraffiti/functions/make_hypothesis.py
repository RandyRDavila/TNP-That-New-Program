from itertools import combinations

from TxGraffiti.classes.hypothesis_class import hypothesis as hyp
from TxGraffiti.graph_data.functions.graph_property_names import property_names, non_regular_property_names


def make_hypothesis(index, regular_exception):
    hypothesis = []
    for i in range(1, index):
        if regular_exception == False:
            for h in combinations(property_names, i):
                h = list(h)
                if i == 1:
                    hypothesis.append(hyp(h[0]))
                elif i == 2:
                    hypothesis.append(hyp(h[0], h[1]))
                else:
                    hypothesis.append(hyp(h[0], h[1], h[2]))
        else:
            for h in combinations(non_regular_property_names, i):
                h = list(h)
                if i == 1:
                    hypothesis.append(hyp(h[0]))
                elif i == 2:
                    hypothesis.append(hyp(h[0], h[1]))
                else:
                    hypothesis.append(hyp(h[0], h[1], h[2]))

    return hypothesis
