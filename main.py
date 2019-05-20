from tnp.functions.make_expressions import *
from itertools import combinations
from tnp.graph_data.functions.graph_property_names import *
from tnp.functions.Theo import Theo
from tnp.functions.make_hypothesis import hypotheses


def make_conjectures_one(target):
    hyp = hypotheses(index=4)
    for h in hyp:
        for i in invariant_names:
            if i != target:
                yield make_ratio(h, target, i, "upper")
                yield make_ratio(h, target, i, "lower")
                yield make_constant(h, target, i, "upper")
                yield make_constant(h, target, i, "lower")


def make_conjectures_two(target):
    hyp = hypotheses(index=3)
    for h in hyp:
        for c in combinations(invariant_names, 2):
            if c[1] != c[0] and c[1] != target and c[0] != target:
                yield make_ratio_two(h, target, c[0], c[1], "upper")
                yield make_ratio_two(h, target, c[0], c[1], "lower")


def make_conjectures_three(target):
    hyp = hypotheses(index=3)
    for h in hyp:
        for c in combinations(invariant_names, 2):
            if c[1] != c[0] and c[1] != target and c[0] != target:
                yield make_ratio_three(h, target, c[0], c[1], "upper")
                yield make_ratio_three(h, target, c[0], c[1], "lower")

    # C = Theo(conjs)
    # return C


def make_conjectures_four(target):
    hyp = hypotheses(index=3)
    for h in hyp:
        for c in combinations(invariant_names, 2):
            if c[1] != c[0] and c[1] != target and c[0] != target:
                yield make_constant_two(h, target, c[0], c[1], "upper")
                yield make_constant_two(h, target, c[0], c[1], "lower")

    # C = Theo(conjs)
    # return C
