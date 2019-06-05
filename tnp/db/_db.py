import itertools
import json
import multiprocessing
import pathlib
import operator

import grinpy as gp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tnp.invariants import invariants
from tnp.properties import properties
from tnp.db.models import Base, Graph


def _calculate(graph):
    return graph, {func.name: func(graph) for func in itertools.chain(invariants, properties)}


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
            return [_graph_from_json(graph.json) for graph in self._query.all()]
        else:
            filters = [(*kwarg.split("__"), kwargs[kwarg]) for kwarg in kwargs]
            expressions = [_to_filter_expression(filter, Graph) for filter in filters]
            results = self._query.filter(*expressions).all()
            return [_graph_from_json(graph.json) for graph in results]

    def all(self):
        return [_graph_from_json(graph.json) for graph in self._query.all()]

    def complete(self):
        return [_graph_from_json(graph.json) for graph in self._query.filter(Graph.is_complete is True)]

    def _build_from_json(self, json_):
        graphs = (_graph_from_json(data) for data in json.loads(json_))
        with multiprocessing.Pool() as pool:
            for graph, calculations in pool.imap(_calculate, graphs):
                data = gp.node_link_data(graph)
                db_graph = Graph(json=data, **calculations)
                self._db_session.add(db_graph)
        self._db_session.commit()

    def _build_from_file(self, path):
        json_ = pathlib.Path(path).read_text()
        self._build_from_json(json_)

    def _create_table(self, json_=None, from_file=None):
        """Build the graphs table from scratch.

            If the graphs table already exists, it will be dropped before building.
            """
        # TODO: Add support for reading from_file from a config file
        # Should also support path-like object, not just string
        if json_ is not None and from_file is not None:
            raise ValueError("Can not provide both `json` and `from_file`")
        elif json_ is not None:
            self._build_from_json(json_)
        elif from_file is not None:
            self._build_from_file(from_file)
        else:
            raise ValueError("One of `json` or `from_file` parameters is required")


class DB:
    def __init__(self, db_path=None):
        # TODO: Add support for reading db_path from config file
        # Should also support path-like objects, not just strings
        _engine = create_engine(f"sqlite:///{db_path}")
        _session = sessionmaker(bind=_engine)
        Base.metadata.create_all(_engine)

        self._engine = _engine
        self._session = _session()

    @property
    def graphs(self):
        return _graphs(self._session)
