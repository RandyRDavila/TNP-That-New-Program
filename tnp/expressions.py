import ast
import functools
import json
import math
import operator
import re
import sympy

import grinpy as gp

from tnp.exceptions import FunctionNotAllowedError, NameNotAllowedError, OperatorNotAllowedError
from tnp.invariants import invariants
import tnp.db.models


class _ASTMathEvaluator:
    _operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
    }

    _functions = {"abs": operator.abs, "sqrt": math.sqrt}

    _names = []

    def __init__(self, namespace: list = None):
        if namespace is not None:
            self._names.extend(namespace)

    def _validate_name(self, node):
        if node.id in self._names:
            return node.id

        raise NameNotAllowedError(node.id)

    def _validate_bin_op(self, node):
        operator = self._operators.get(type(node.op))
        if operator is not None:
            return self._validate(node.left) and (self._validate(node.right))

        raise OperatorNotAllowedError(node.op)

    def _validate_unary_op(self, node):
        operator = self._operators.get(type(node.op))
        if operator is not None:
            return self._validate(node.operand)

        raise OperatorNotAllowedError(node.op)

    def _validate_function(self, node):
        func = self._functions.get(node.func.id)
        if func is not None:
            args_are_valid = all([self._validate(arg) for arg in node.args])
            kwargs_are_valid = all([self._validate(keyword.value) for keyword in node.keywords])
            return args_are_valid and kwargs_are_valid

        raise FunctionNotAllowedError(node.func.id)

    def _validate(self, node):
        if isinstance(node, ast.Num):
            return True
        elif isinstance(node, ast.Name):
            return self._validate_name(node)
        elif isinstance(node, ast.BinOp):
            return self._validate_bin_op(node)
        elif isinstance(node, ast.UnaryOp):
            return self._validate_unary_op(node)
        elif isinstance(node, ast.Call):
            return self._validate_function(node)

        raise TypeError(node)

    def validate(self, expression):
        parsed_expression = ast.parse(expression, mode="eval")
        return self._validate(parsed_expression.body)

    def _ast_to_op(self, ast_op):
        _op = self._operators.get(ast_op)
        if _op is not None:
            return _op

        raise OperatorNotAllowedError(str(ast_op))

    def _ast_to_func(self, ast_func):
        func = self._functions.get(ast_func.id)
        if func is not None:
            return func

        raise FunctionNotAllowedError(ast_func.id)

    def _ast_to_name(self, ast_name):
        if ast_name in self._names:
            return ast_name

        raise NameNotAllowedError(ast_name)

    def _eval_bin_op(self, node):
        operator_ = self._ast_to_op(type(node.op))
        left_operand = self.eval_(node.left)
        right_operand = self.eval_(node.right)
        return operator_(left_operand, right_operand)

    def _eval_unary_op(self, node):
        operator_ = self._ast_to_op(type(node.op))
        operand = self.eval_(node.operand)
        return operator_(operand)

    def _eval_function(self, node):
        func = self._ast_to_func(node.func)
        args = [self.eval_(arg) for arg in node.args]
        kwargs = {keyword.arg: keyword.value for keyword in node.keywords}
        return func(*args, **kwargs)

    def _eval_name(self, node):
        return self._ast_to_name(node.id)

    def eval_(self, node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Name):
            return self._eval_name(node)
        elif isinstance(node, ast.BinOp):
            return self._eval_bin_op(node)
        elif isinstance(node, ast.UnaryOp):
            return self._eval_unary_op(node)
        elif isinstance(node, ast.Call):
            return self._eval_function(node)

        raise TypeError(node)

    def evaluate(self, expression):
        parsed_expression = ast.parse(expression, mode="eval")
        return self.eval_(parsed_expression.body)


SYMPY_NAMESPACE = {invariant.name: sympy.Symbol(invariant.name) for invariant in invariants}


class Expression:
    """Class for representing mathematical expressions"""

    def __init__(self, expression: str):
        self._evaluator = _ASTMathEvaluator(namespace=list(invariants.names))
        self._evaluator.validate(expression)
        self._string = expression
        self._touch_number_cache = {}
        self._simplified = None

    def __repr__(self):
        return f"{self.__class__.__name__}(expression={self._string!r})"

    def __str__(self, simplified=False):
        return self._string

    @property
    def simplified(self):
        if self._simplified is None:
            sympified = sympy.sympify(self._string, locals=SYMPY_NAMESPACE)
            self._simplified = str(sympy.simplify(sympified))

        return self._simplified

    def evaluate(self, graph, db=None):
        def _invariant_value(graph, matchobj):
            invariant_name = matchobj.group(0)
            invariant = invariants[invariant_name]

            # Check that graph is a NetworkX graph or a TNP Graph model instance
            if not isinstance(graph, (gp.Graph, tnp.db.models.Graph)):
                raise TypeError("Invalid graph type; must be NetworkX graph or tnp.db.models.Graph instance")

            # If the graph is a TNP Graph model instance, return the stored invariant value
            # or calculate the value if no stored value is found
            if isinstance(graph, tnp.db.models.Graph):
                if hasattr(graph, invariant_name):
                    return str(getattr(graph, invariant_name))
                else:
                    nxgraph = gp.node_link_graph(json.loads(graph.json))
                    return str(invariant(nxgraph))

            # If the graph is a NetworkX graph, use the node-link data to try and look up
            # the graph in the database and return either the stored value
            if db is not None:
                json_query = json.dumps(gp.node_link_data(graph))
                results = db.graphs(json_=json_query)
                if results:
                    db_graph = results[0]
                    if hasattr(db_graph, invariant_name):
                        return str(getattr(db_graph, invariant_name))

            # If no database value is found, or no database is passed, return the calculated
            # invariant value
            return str(invariant(graph))

        prepared_expression = re.sub(
            pattern=rf"\b({'|'.join(f.name for f in invariants)})\b",
            repl=functools.partial(_invariant_value, graph),
            string=self._string,
        )
        return self._evaluator.evaluate(prepared_expression)

    def __call__(self, graph):
        return self.evaluate(graph)

    def touch_number(self, comparison_invariant, graphs):
        cache_key = hash((comparison_invariant.name, tuple(graphs)))

        touch_number = self._touch_number_cache.get(cache_key)
        if touch_number is None:

            def _calculate(invariant, graph):
                if isinstance(graph, tnp.db.models.Graph):
                    if hasattr(graph, invariant.name):
                        return getattr(graph, invariant.name)
                    else:
                        graph = gp.node_link_graph(json.loads(graph.json))
                        return invariant(graph)
                else:
                    return invariant(graph)

            touch_number = sum(_calculate(comparison_invariant, graph) == self.evaluate(graph) for graph in graphs)
            self._touch_number_cache = {cache_key: touch_number}

        return touch_number

    def __lt__(self, other):
        return self.touch_number() < other.touch_number()

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.simplified)
