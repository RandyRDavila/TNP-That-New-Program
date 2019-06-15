from typing import Iterable

import sortedcontainers

from tnp.db.models import Conjecture, Graph


class Heuristic:
    def apply(self, conjectures: Iterable[Conjecture], graphs: Iterable[Graph]) -> Iterable[Conjecture]:
        return NotImplemented


class Touched(Heuristic):
    def apply(self, conjectures: Iterable[Conjecture], graphs: Iterable[Graph]) -> Iterable[Conjecture]:
        def _touch_number(conjecture):
            _target = conjecture.target_invariant
            return conjecture.right_hand_side.touch_number(_target, graphs)

        sorted_conjectures = sortedcontainers.SortedList([], key=lambda x: _touch_number(x))
        sorted_conjectures.update(conjectures)
        return iter(reversed(sorted_conjectures))
