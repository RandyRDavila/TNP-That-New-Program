import grinpy as gp
import pytest

from tnp.expressions import _ASTMathEvaluator, Expression
from tnp.exceptions import FunctionNotAllowedError, NameNotAllowedError, OperatorNotAllowedError


class Test_ASTMathEvaluator:
    @pytest.mark.parametrize(
        "expression, expected_value",
        (("1 + 1", 2), ("1 + (-1)", 0), ("20 - 10 / 5", 18), ("(20 - 10) / 5", 2), ("abs(-10)", 10), ("sqrt(4)", 2)),
    )
    def test_evaluates_expressions_correctly(self, expression, expected_value):
        evaluator = _ASTMathEvaluator()
        assert evaluator.evaluate(expression) == expected_value

    @pytest.mark.parametrize("expression", ("one", "1 + independence_number", "two / 3"))
    def test_evaluating_unknown_name_raises_NameNotAllowedError(self, expression):
        evaluator = _ASTMathEvaluator()
        with pytest.raises(NameNotAllowedError):
            evaluator.evaluate(expression)

    @pytest.mark.parametrize("expression", ("1 >> 2", "not True"))
    def test_evaluating_unknown_operator_raises_OperatorNotAllowedError(self, expression):
        evaluator = _ASTMathEvaluator()
        with pytest.raises(OperatorNotAllowedError):
            evaluator.evaluate(expression)

    @pytest.mark.parametrize("expression", ("help(x)", "dir(x)"))
    def test_evaluating_unknown_function_raises_FunctionNotAllowedError(self, expression):
        evaluator = _ASTMathEvaluator()
        with pytest.raises(FunctionNotAllowedError):
            evaluator.evaluate(expression)

    @pytest.mark.parametrize(
        "expression", ("1 + 1", "1 + (-1)", "20 - 10 / 5", "(20 - 10) / 5", "abs(-10)", "sqrt(4)")
    )
    def test_validates_expressions_correctly(self, expression):
        evaluator = _ASTMathEvaluator()
        assert evaluator.validate(expression) is True

    @pytest.mark.parametrize("expression", ("one", "1 + independence_number", "two / 3"))
    def test_validating_unknown_name_raises_NameNotAllowedError(self, expression):
        evaluator = _ASTMathEvaluator()
        with pytest.raises(NameNotAllowedError):
            evaluator.validate(expression)

    @pytest.mark.parametrize("expression", ("1 >> 2", "not True"))
    def test_validating_unknown_operator_raises_OperatorNotAllowedError(self, expression):
        evaluator = _ASTMathEvaluator()
        with pytest.raises(OperatorNotAllowedError):
            evaluator.validate(expression)

    @pytest.mark.parametrize("expression", ("help(x)", "dir(x)"))
    def test_validating_unknown_function_raises_FunctionNotAllowedError(self, expression):
        evaluator = _ASTMathEvaluator()
        with pytest.raises(FunctionNotAllowedError):
            evaluator.validate(expression)


class TestExpression:
    @pytest.mark.parametrize(
        "expression, graph, expected_value",
        (
            ("1 + 1", gp.complete_graph(3), "1 + 1"),
            ("1 + independence_number", gp.complete_graph(3), "1 + 1"),
            ("1 + domination_number", gp.complete_graph(3), "1 + 1"),
        ),
    )
    def test_prepare_return_correct_string(self, expression, graph, expected_value):
        expr = Expression(expression)
        assert expr._prepare(graph) == expected_value

    @pytest.mark.parametrize(
        "expression, graph, expected_value",
        (
            ("1 + 1", gp.complete_graph(3), 2),
            ("2 + independence_number", gp.complete_graph(3), 3),
            ("4 - 3 * domination_number", gp.complete_graph(3), 1),
        ),
    )
    def test_evaluates_correctly(self, expression, graph, expected_value):
        expr = Expression(expression)
        assert expr.evaluate(graph) == expected_value
