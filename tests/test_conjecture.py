import pytest

from tnp.classes.conjecture_class import Conjecture


class TestConjecture:
    def test_instance_assigns_correct_attributes(self):
        conjecture = Conjecture("hypothesis", "target", "inequality", "expression")
        assert conjecture.hyp == "hypothesis"
        assert conjecture.target == "target"
        assert conjecture.inequality == "inequality"
        assert conjecture.expression == ["expression"]

    @pytest.mark.parametrize("expression, expected_value", (("", ""), ("1", "1"), ("1 2", "1 2")))
    def test_get_expressions_returns_correct_string(self, expression, expected_value):
        conjecture = Conjecture(None, None, None, expression)
        assert conjecture.get_expression() == expected_value

    def test_str_returns_correct_string(self):
        conjecture = Conjecture("hypothesis", "target", "inequality", "expression")
        assert str(conjecture) == "If hypothesis, then target inequality expression"

    def test_repr_returns_correct_string(self):
        conjecture = Conjecture("hypothesis", "target", "inequality", "expression")
        expected_string = (
            "Conjecture(hypothesis='hypothesis', target='target', inequality='inequality', expression='expression')"
        )
        assert repr(conjecture) == expected_string
