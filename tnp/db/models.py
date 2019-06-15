from sqlalchemy import Boolean, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

import grinpy as gp

from tnp.db.types import ConjectureType, Expression, HypothesesList, Invariant
from tnp.invariants import invariants
from tnp.properties import properties


Base = declarative_base()

Graph = type(
    "Graph",
    (Base,),
    {
        "__tablename__": "graphs",
        "id": Column(Integer, primary_key=True),
        "json": Column(String),
        **{invariant: Column(Float) for invariant in invariants.names},
        **{prop: Column(Boolean) for prop in properties.names},
    },
)


class Conjecture(Base):
    __tablename__ = "conjectures"

    id = Column(Integer, primary_key=True)
    type = Column(ConjectureType)
    hypotheses = Column(HypothesesList)
    target_invariant = Column(Invariant)
    right_hand_side = Column(Expression)

    def __repr__(self):
        _name = self.__class__.__name__
        _type = self.type
        _hyp = self.hypotheses
        _target = self.target_invariant
        _expr = self.right_hand_side
        return f"{_name}(type={_type!r}, hypotheses={_hyp!r}, target_invariant={_target!r}, expression={_expr!r})"

    def __str__(self) -> None:
        _target = self.target_invariant
        _operator = self.type[1]
        _expr = self.right_hand_side.simplified

        if self.hypotheses:
            _hyp = self.hypotheses = [p.name for p in self.hypotheses]
            return f"If G {', '.join(_hyp)}, then {_target} {_operator} {_expr}."
        else:
            return f"For all graphs, {_target} {_operator} {_expr}."

    @property
    def operator(self) -> str:
        return self.type[0]

    def _graph_satisfies_hypotheses(self, graph: gp.Graph) -> bool:
        return all((property_(graph) for property_ in self.hypotheses))

    def is_satisfied_by(self, graph: gp.Graph) -> bool:
        """Return True is `graph` satisfies the conjecture, False otherwise."""
        if not self._graph_satisfies_hypotheses(graph):
            return False

        _op = self.operator
        _target_value = self.target_invariant(graph)
        _expression_value = self.right_hand_side.evaluate(graph)
        return _op(_target_value, _expression_value)
