from itertools import combinations, islice

from tnp.classes.hypothesis_class import hypothesis as hyp
from tnp.graph_data.functions.graph_property_names import property_names


def hypotheses(index):
    _hypotheses = []
    for i in range(1, index):
        for h in combinations(property_names, i):
            terms = tuple(islice(h, i))
            _hypotheses.append(hyp(*terms))
    return _hypotheses
