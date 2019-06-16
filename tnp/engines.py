from fractions import Fraction
import functools
import itertools
import math
import multiprocessing
import operator
from typing import Iterable, Set

import numpy as np

from tnp.db._db import DB
from tnp.db.models import Conjecture, Graph
from tnp.expressions import Expression
from tnp.heuristics import Heuristic
from tnp.invariants import Invariant, invariants
from tnp.properties import Property

UPPER_BOUND = (operator.le, "<=")
LOWER_BOUND = (operator.ge, ">=")


class ConjectureEngine:
    def __init__(
        self,
        type: tuple,
        target_invariant: Invariant,
        graphs: Iterable[Graph] = None,
        hypotheses: Iterable[Property] = (),
        heuristic: Heuristic = None,
    ) -> None:
        self.type = type
        self.hypotheses = tuple(hypotheses)
        self.target_invariant = target_invariant
        if graphs is None:
            db = DB("tnp.db")
            self.graphs = db.graphs(**{p.name: True for p in self.hypotheses})
        else:
            self.graphs = graphs
        self.heuristic = heuristic
        self.conjectures = ()

    def __repr__(self):
        _name = self.__class__.__name__
        _type = self.type
        _hyp = self.hypotheses
        _target = self.target_invariant
        _graphs = self.graphs
        _heuristic = self.heuristic
        return f"{_name}(type={_type!r}, hypotheses={_hyp!r}, target_invariant={_target!r}, graphs={_graphs!r}, heuristic={_heuristic})"

    def get_starting_points(self):
        return NotImplemented

    def generate_expressions(self, starting_points: Iterable) -> Iterable[Expression]:
        return NotImplemented

    def filter_by_transitivity(self, conjectures: Iterable[Conjecture]):
        conjectures = tuple(conjectures)
        conjecture_values = {
            hash(conjecture): np.array([conjecture.right_hand_side.evaluate(graph) for graph in self.graphs])
            for conjecture in conjectures
        }
        _op = self.type[0]

        for hash1 in tuple(conjecture_values):
            array1 = conjecture_values.get(hash1)
            if array1 is None:
                continue
            for hash2 in set(conjecture_values) - {hash1}:
                array2 = conjecture_values.get(hash2)
                if array2 is not None and all(_op(array1, array2)):
                    conjecture_values.pop(hash2, None)

        return (conjecture for conjecture in conjectures if hash(conjecture) in conjecture_values)

    def make_conjectures(self, cache_results=True, filter_by_transitivity=True):
        with multiprocessing.Pool() as pool:
            _generate = self.generate_expressions
            _expressions_by_starting_point = pool.imap(_generate, self.get_starting_points())
            expressions = itertools.chain(*_expressions_by_starting_point)

        # Convert generated expressions into Conjecture objects
        conjectures = (
            Conjecture(
                type=self.type,
                hypotheses=self.hypotheses,
                target_invariant=self.target_invariant,
                right_hand_side=expression,
            )
            for expression in expressions
            if expression is not None
        )

        # Remove any conjectures that don't hold for the engine's set of graphs
        conjectures = (
            conjecture for conjecture in conjectures if all(conjecture.is_satisfied_by(graph) for graph in self.graphs)
        )

        # Filter conjecture by transitivity if necessary
        if filter_by_transitivity is True:
            conjectures = self.filter_by_transitivity(conjectures)

        # Apply the heuristic if necessary
        if self.heuristic is not None:
            conjectures = self.heuristic.apply(conjectures, self.graphs)

        # Cache results if necessary
        if cache_results is True:
            self.conjectures = tuple(conjectures)
            return iter(self.conjectures)

        return conjectures


class LinearApproximator(ConjectureEngine):
    def get_starting_points(self) -> Iterable:
        return itertools.chain(*(itertools.combinations(set(invariants) - {self.target_invariant}, n) for n in (1, 2)))

    def _linear_approximation(self, expression: Expression) -> Expression:
        target_values = np.array([float(self.target_invariant(graph)) for graph in self.graphs])
        expr_values = np.array([float(expression.evaluate(graph)) for graph in self.graphs])

        # Ignore invariants that are undefnied for some some graph in `graphs`
        if 0 in expr_values:
            return None

        ratios = target_values / expr_values
        if self.type == UPPER_BOUND:
            optimal_ratio = ratios[ratios < math.inf].max()
        else:
            optimal_ratio = ratios[ratios > -math.inf].min()

        # We want to keep numbers small in the conjectures,
        # so discard any expression with a slope greater than 3
        if 0 < abs(optimal_ratio) < 1 / 5 or 3 < abs(optimal_ratio):
            return None

        slope = Fraction(optimal_ratio).limit_denominator(1000)
        ratios = slope * expr_values

        if self.type == UPPER_BOUND:
            intercept = (target_values - ratios).max()
        else:
            intercept = (target_values - ratios).min()

        if 0 < abs(intercept) < 1 / 5 or 3 < abs(intercept):
            return None

        expr_string = f"{slope} * {expression} + {intercept}"
        optimal_expression = Expression(expr_string)

        # Calculate the touch_number and simplified expression (values are cached)
        optimal_expression.touch_number(self.target_invariant, self.graphs)
        optimal_expression.simplified

        return optimal_expression

    def generate_expressions(self, invariants: Iterable[Invariant]) -> Set[Expression]:
        invariants = tuple(invariants)
        lin_approx = self._linear_approximation
        num_invariants = len(invariants)
        expressions = set()

        if num_invariants == 1:
            expressions.add(lin_approx(Expression(f"{invariants[0]}")))
        if num_invariants == 2:
            a, b = invariants
            sets = (set(), set(), set(), set())
            for i, j in itertools.product((3, 2, 1), (3, 2, 1)):
                strings = (
                    f"abs({i} * {a} - {j} * {b})",
                    f"(({a} + {i}) / ({b} + {j}))",
                    f"(({b} + {i}) / ({a} + {j}))",
                    f"({a} * {b})",
                )
                for set_, string in zip(sets, strings):
                    try:
                        expression = lin_approx(Expression(string))
                    except (ValueError, ZeroDivisionError):
                        pass

                    if expression is not None:
                        set_.add(expression)

            def _most_general_expression(expr1, expr2):
                arrays = [
                    np.array([expression.evaluate(graph) for graph in self.graphs]) for expression in (expr1, expr2)
                ]
                _op = self.type[0]
                if _op(arrays[1].max(), arrays[0].max()):
                    return expr1
                else:
                    return expr2

            return {functools.reduce(_most_general_expression, set_) for set_ in sets if len(set_) > 0}

        return expressions
