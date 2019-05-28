from unittest.mock import MagicMock

import grinpy as gp
import pytest

from tnp.properties import Property, properties


_properties = {
    "is_bipartite": Property(function=gp.is_bipartite),
    "is_chordal": Property(function=gp.is_chordal),
    "has_bridges": Property(function=gp.has_bridges),
    "is_connected": Property(function=gp.is_connected),
    "is_distance_regular": Property(function=gp.is_distance_regular),
    "is_strongly_regular": Property(function=gp.is_strongly_regular),
    "is_eulerian": Property(function=gp.is_eulerian),
    "is_planar": Property(function=lambda G: gp.check_planarity(G)[0], name="is_planar"),
    "is_regular": Property(function=gp.is_regular),
    "is_cubic": Property(function=gp.is_cubic),
    "is_not_K_n": Property(function=lambda G: not gp.is_complete_graph(G), name="is_not_K_n"),
    "is_triangle_free": Property(function=gp.is_triangle_free),
}


class TestPropertyClass:
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
        """Ensure instantiating Property without a callable raises a TypeError"""
        with pytest.raises(TypeError):
            Property(function=function)

    @pytest.mark.parametrize(
        "name", (1, (), {}, [], True, type), ids=("name=1", "name=()", "name={}", "name=[]", "name=True", "name=type")
    )
    def test_instantiation_without_name_string_raises_TypeError(self, name):
        """Ensure instantiating Property with `name` that isn't a string raises a TypeError"""
        with pytest.raises(TypeError):
            Property(function=type, name=name)

    @pytest.mark.parametrize("attribute", ("function", "name", "_name"))
    def test_has_attributes(self, attribute):
        """Ensure Property instances have the expected attributes"""
        _property = Property(function=type, name="test")
        assert hasattr(_property, attribute)

    def test_instantiating_stores_data_in_correct_attributes(self):
        """Ensure Property instances have data stored in correct attributes"""
        _property = Property(function=type, name="test")
        assert _property.function == type
        assert _property._name == "test"

    def test_repr_returns_correct_string(self):
        """Ensure Property.__repr__ returns the correct string"""
        _property = Property(function=type, name="test")
        assert repr(_property) == f"Property(function={type!r}, name='test')"

    @pytest.mark.parametrize(
        "_property, expected_value",
        ((Property(function=type), "type"), (Property(function=type, name="test"), "test")),
    )
    def test_str_returns_correct_string(self, _property, expected_value):
        """Ensure Property.__str__ returns the correct string"""
        assert str(_property) == expected_value

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
        """Ensure Property.__call__ passes args to Property.function"""
        _property = Property(function=mock_function)
        assert _property(*args, **kwargs) == mock_function.return_value
        mock_function.assert_called_once_with(*args, **kwargs)

    @pytest.mark.parametrize(
        "_property, expected_value",
        ((Property(function=type), "type"), (Property(function=type, name="test"), "test")),
    )
    def test_name_returns_correct_string(self, _property, expected_value):
        """Ensure Property.__str__ returns the correct string"""
        assert _property.name == expected_value

    @pytest.mark.parametrize(
        "invariant1, invariant2, expected_value",
        (
            (Property(function=type), Property(function=type), True),
            (Property(function=type), Property(function=help), False),
            (Property(function=type, name="type"), Property(function=type, name="help"), False),
        ),
    )
    def test_eq(self, invariant1, invariant2, expected_value):
        assert (invariant1 == invariant2) is expected_value


class TestProperties:
    def test_iterator(self):
        assert tuple(properties) == tuple(value for _, value in _properties.items())

    def test_contains_correct_invariants(self):
        assert dict(zip(properties.names, properties)) == _properties

    @pytest.mark.parametrize(
        "invariant_name, expected_value",
        tuple(zip((key for key, value in _properties.items()), (value for _, value in _properties.items()))),
        ids=tuple(key for key, value in _properties.items()),
    )
    def test_getattr(self, invariant_name, expected_value):
        assert getattr(properties, invariant_name) == expected_value

    def test_getattr_raises_AttributeError(self):
        with pytest.raises(AttributeError):
            properties.abracadabra

    @pytest.mark.parametrize(
        "invariant_name, expected_value",
        tuple(zip((key for key, value in _properties.items()), (value for _, value in _properties.items()))),
        ids=tuple(key for key, value in _properties.items()),
    )
    def test_getitem(self, invariant_name, expected_value):
        assert properties[invariant_name] == expected_value

    def test_getitem_raises_KeyError(self):
        with pytest.raises(KeyError):
            properties["abracadabra"]
