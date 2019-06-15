from collections import abc
import functools
import json
from typing import Callable

import grinpy as gp

import tnp.db.models


class _GraphCallable:
    def __init__(self, function: Callable, name: str = None) -> None:
        if not isinstance(function, abc.Callable):
            raise TypeError("function must be callable")

        if name is not None and not isinstance(name, str):
            raise TypeError("name must be a string")

        self.function = function
        self._name = name

    def __repr__(self) -> None:
        return f"{self.__class__.__name__}(function={self.function!r}, name={self._name!r})"

    def __str__(self) -> None:
        return self.name

    def __eq__(self, other) -> None:
        return (self.function == other.function) and (self.name == other.name)

    def __hash__(self):
        return hash(str(self))

    @functools.lru_cache(maxsize=None)
    def __call__(self, graph, *args, **kwargs) -> None:
        if isinstance(graph, tnp.db.models.Graph):
            if hasattr(graph, self.name):
                return getattr(graph, self.name)
            else:
                graph = gp.node_link_graph(json.loads(graph.json))

        return self.function(graph, *args, **kwargs)

    @property
    def name(self) -> None:
        return self.function.__name__ if self._name is None else self._name


class _NamespaceIterator:
    def __init__(self) -> None:
        self._names = tuple(key for key, value in self.namespace.__dict__.items() if isinstance(value, self.type))

    def __getattr__(self, attribute: str):
        try:
            return getattr(self.namespace, attribute)
        except AttributeError as exc:
            raise AttributeError(exc) from None

    def __getitem__(self, item):
        try:
            return self.namespace.__dict__[item]
        except KeyError as exc:
            raise KeyError(exc) from None

    def __iter__(self):
        self._itr = (value for _, value in self.namespace.__dict__.items() if isinstance(value, self.type))
        return self

    def __next__(self):
        return next(self._itr)

    @property
    def names(self):
        return self._names
