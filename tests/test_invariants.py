import pytest
from unittest.mock import MagicMock

import grinpy as gp

from tnp.invariants import Invariant, invariants


_invariants = {
    "domination_number": Invariant(function=gp.domination_number),
    "total_domination_number": Invariant(function=gp.total_domination_number),
    "connected_domination_number": Invariant(function=gp.connected_domination_number),
    "independence_number": Invariant(function=gp.independence_number),
    "power_domination_number": Invariant(function=gp.power_domination_number),
    "zero_forcing_number": Invariant(function=gp.zero_forcing_number),
    "total_zero_forcing_number": Invariant(function=gp.total_zero_forcing_number),
    "connected_zero_forcing_number": Invariant(function=gp.connected_zero_forcing_number),
    "diameter": Invariant(function=gp.diameter),
    "radius": Invariant(function=gp.radius),
    "order": Invariant(function=gp.number_of_nodes, name="order"),
    "size": Invariant(function=gp.number_of_edges, name="size"),
    "independent_domination_number": Invariant(function=gp.independent_domination_number),
    "chromatic_number": Invariant(function=gp.chromatic_number),
    "matching_number": Invariant(function=gp.matching_number),
    "min_maximal_matching_number": Invariant(function=gp.min_maximal_matching_number),
    "triameter": Invariant(function=gp.triameter),
    "randic_index": Invariant(function=gp.randic_index),
    "augmented_randic_index": Invariant(function=gp.augmented_randic_index),
    "harmonic_index": Invariant(function=gp.harmonic_index),
    "atom_bond_connectivity_index": Invariant(function=gp.atom_bond_connectivity_index),
    "sum_connectivity_index": Invariant(function=gp.sum_connectivity_index),
    "min_degree": Invariant(function=gp.min_degree),
    "max_degree": Invariant(function=gp.max_degree),
    "number_of_min_degree_nodes": Invariant(function=gp.number_of_min_degree_nodes),
    "number_of_max_degree_nodes": Invariant(function=gp.number_of_max_degree_nodes),
    "clique_number": Invariant(function=gp.clique_number),
    "residue": Invariant(function=gp.residue),
    "annihilation_number": Invariant(function=gp.annihilation_number),
}


class TestInvariantClass:
    @pytest.mark.parametrize(
        "function",
        (None, 1, (), {}, [], "", True),
        ids=(
            "function=None",
            "function=1",
            "function=()",
            "function={}",
            "function=[]",
            "function=''",
            "function=True",
        ),
    )
    def test_instantation_without_callable_raises_TypeError(self, function):
        """Ensure instantiating Invariant without a callable raises a TypeError"""
        with pytest.raises(TypeError):
            Invariant(function=function)

    @pytest.mark.parametrize(
        "name", (1, (), {}, [], True, type), ids=("name=1", "name=()", "name={}", "name=[]", "name=True", "name=type")
    )
    def test_instantiation_without_name_string_raises_TypeError(self, name):
        """Ensure instantiating Invariant with `name` that isn't a string raises a TypeError"""
        with pytest.raises(TypeError):
            Invariant(function=type, name=name)

    @pytest.mark.parametrize("attribute", ("function", "name", "_name"))
    def test_has_attributes(self, attribute):
        """Ensure Invariant instances have the expected attributes"""
        invariant = Invariant(function=type, name="test")
        assert hasattr(invariant, attribute)

    def test_instantiating_stores_data_in_correct_attributes(self):
        """Ensure Invariant instances have data stored in correct attributes"""
        invariant = Invariant(function=type, name="test")
        assert invariant.function == type
        assert invariant._name == "test"

    def test_repr_returns_correct_string(self):
        """Ensure Invariant.__repr__ returns the correct string"""
        invariant = Invariant(function=type, name="test")
        assert repr(invariant) == f"Invariant(function={type!r}, name='test')"

    @pytest.mark.parametrize(
        "invariant, expected_value",
        ((Invariant(function=type), "type"), (Invariant(function=type, name="test"), "test")),
    )
    def test_str_returns_correct_string(self, invariant, expected_value):
        """Ensure Invariant.__str__ returns the correct string"""
        assert str(invariant) == expected_value

    @pytest.mark.parametrize(
        "mock_function, args, kwargs",
        (
            (MagicMock(return_value=10), (), {}),
            (MagicMock(return_value=10), (1, 2), {}),
            (MagicMock(return_value=10), (), {"arg1": 1, "arg2": 2}),
            (MagicMock(return_value=10), (1, 2), {"arg1": 1, "arg2": 2}),
        ),
    )
    def test_call_calls_function(self, mock_function, args, kwargs):
        """Ensure Invariant.__call__ passes args to Invariant.function"""
        invariant = Invariant(function=mock_function)
        assert invariant(*args, **kwargs) == mock_function.return_value
        mock_function.assert_called_once_with(*args, **kwargs)

    @pytest.mark.parametrize(
        "invariant, expected_value",
        ((Invariant(function=type), "type"), (Invariant(function=type, name="test"), "test")),
    )
    def test_name_returns_correct_string(self, invariant, expected_value):
        """Ensure Invariant.__str__ returns the correct string"""
        assert invariant.name == expected_value

    @pytest.mark.parametrize(
        "invariant1, invariant2, expected_value",
        (
            (Invariant(function=type), Invariant(function=type), True),
            (Invariant(function=type), Invariant(function=help), False),
            (Invariant(function=type, name="type"), Invariant(function=type, name="help"), False),
        ),
    )
    def test_eq(self, invariant1, invariant2, expected_value):
        assert (invariant1 == invariant2) is expected_value


class TestInvariants:
    def test_iterator(self):
        assert tuple(invariants) == tuple(value for _, value in _invariants.items())

    def test_contains_correct_invariants(self):
        assert dict(zip(invariants.names, invariants)) == _invariants

    @pytest.mark.parametrize(
        "invariant_name, expected_value",
        tuple(zip((key for key, value in _invariants.items()), (value for _, value in _invariants.items()))),
        ids=tuple(key for key, value in _invariants.items()),
    )
    def test_getattr(self, invariant_name, expected_value):
        assert getattr(invariants, invariant_name) == expected_value

    def test_getattr_raises_AttributeError(self):
        with pytest.raises(AttributeError):
            invariants.abracadabra

    @pytest.mark.parametrize(
        "invariant_name, expected_value",
        tuple(zip((key for key, value in _invariants.items()), (value for _, value in _invariants.items()))),
        ids=tuple(key for key, value in _invariants.items()),
    )
    def test_getitem(self, invariant_name, expected_value):
        assert invariants[invariant_name] == expected_value

    def test_getitem_raises_KeyError(self):
        with pytest.raises(KeyError):
            invariants["abracadabra"]
