import json
import operator

import grinpy as gp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from tnp.db.models import Base, Graph


def _graph_from_json(json_):
    return gp.node_link_graph(json.loads(json_))


def _to_op(op):
    _op = {
        "eq": operator.eq,
        "ge": operator.ge,
        "gt": operator.gt,
        "le": operator.le,
        "lt": operator.lt,
        "ne": operator.ne,
    }.get(op)

    if _op is not None:
        return _op

    raise ValueError("Invalid lookup expression operator")


def _to_filter_expression(filter, model):
    if len(filter) == 2:
        field, value = filter
        return getattr(model, field) == value
    elif len(filter) == 3:
        field, op, value = filter
        op = _to_op(op)
        return op(getattr(model, field), value)
    else:
        raise ValueError("Lookup expression depth too deep")


class _graphs:
    def __init__(self, db_session):
        self._db_session = db_session
        self._query = db_session.query(Graph)

    def __call__(self, **kwargs):
        if not kwargs:
            return [graph for graph in self._query.all()]
        else:
            filters = [(*kwarg.split("__"), kwargs[kwarg]) for kwarg in kwargs]
            expressions = [_to_filter_expression(filter, Graph) for filter in filters]
            results = self._query.filter(*expressions).all()
            return [graph for graph in results]

    def all(self):
        return [graph for graph in self._query.all()]

    def complete(self):
        return [graph for graph in self._query.filter(Graph.is_complete is True)]


class DB:
    def __init__(self, db_path=None):
        # TODO: Add support for reading db_path from config file
        # Should also support path-like objects, not just strings
        _engine = create_engine(
            f"sqlite:///{db_path}", connect_args={"check_same_thread": False}, poolclass=StaticPool
        )
        _session = sessionmaker(bind=_engine)
        Base.metadata.create_all(_engine)

        self._engine = _engine
        self._session = _session()

    @property
    def graphs(self):
        return _graphs(self._session)
