from tnp.classes.conjecture_class import Conjecture


class TestConjecture:
    def test_instance_assigns_correct_attributes(self):
        conjecture = Conjecture("hypothesis", "target", "inequality", "expression")
        assert conjecture.hyp == "hypothesis"
        assert conjecture.target == "target"
        assert conjecture.inequality == "inequality"
        assert conjecture.expression == "expression"
