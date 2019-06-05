import ast
import functools
import math
import operator
import re

from typing import Callable

from tnp.exceptions import FunctionNotAllowedError, NameNotAllowedError, OperatorNotAllowedError
from tnp.invariants import invariants


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


class Expression:
    """Class for representing mathematical expressions"""

    def __init__(self, expression: str):
        self._evaluator = _ASTMathEvaluator(namespace=list(invariants.names))
        self._evaluator.validate(expression)
        self._string = expression

    def _calculate_matched_invariant(self, graph, matchobj):
        invariant_name = matchobj.group(0)
        invariant = invariants[invariant_name]
        return str(invariant(graph))

    def __repr__(self):
        return f"{self.__class__.__name__}(expression={self._string!r})"

    def __str__(self):
        return self._string

    def _prepare(self, graph):
        return re.sub(
            pattern=rf"\b({'|'.join(f.name for f in invariants)})\b",
            repl=functools.partial(self._calculate_matched_invariant, graph),
            string=self._string,
        )

    def evaluate(self, graph):
        prepared_expression = self._prepare(graph)
        return self._evaluator.evaluate(prepared_expression)
