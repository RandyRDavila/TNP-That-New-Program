from unittest.mock import MagicMock

import pytest

from tnp._base_classes import _GraphCallable


class TestGraphCallable:
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
        """Ensure instantiating _GraphCallable without a callable raises a TypeError"""
        with pytest.raises(TypeError):
            _GraphCallable(function=function)

    @pytest.mark.parametrize(
        "name", (1, (), {}, [], True, type), ids=("name=1", "name=()", "name={}", "name=[]", "name=True", "name=type")
    )
    def test_instantiation_without_name_string_raises_TypeError(self, name):
        """Ensure instantiating _GraphCallable with `name` that isn't a string raises a TypeError"""
        with pytest.raises(TypeError):
            _GraphCallable(function=type, name=name)

    @pytest.mark.parametrize("attribute", ("function", "name", "_name"))
    def test_has_attributes(self, attribute):
        """Ensure _GraphCallable instances have the expected attributes"""
        graph_callable = _GraphCallable(function=type, name="test")
        assert hasattr(graph_callable, attribute)

    def test_instantiating_stores_data_in_correct_attributes(self):
        """Ensure _GraphCallable instances have data stored in correct attributes"""
        graph_callable = _GraphCallable(function=type, name="test")
        assert graph_callable.function == type
        assert graph_callable._name == "test"

    def test_repr_returns_correct_string(self):
        """Ensure _GraphCallable.__repr__ returns the correct string"""
        graph_callable = _GraphCallable(function=type, name="test")
        assert repr(graph_callable) == f"_GraphCallable(function={type!r}, name='test')"

    @pytest.mark.parametrize(
        "graph_callable, expected_value",
        ((_GraphCallable(function=type), "type"), (_GraphCallable(function=type, name="test"), "test")),
    )
    def test_str_returns_correct_string(self, graph_callable, expected_value):
        """Ensure _GraphCallable.__str__ returns the correct string"""
        assert str(graph_callable) == expected_value

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
        """Ensure _GraphCallable.__call__ passes args to _GraphCallable.function"""
        graph_callable = _GraphCallable(function=mock_function)
        assert graph_callable(*args, **kwargs) == mock_function.return_value
        mock_function.assert_called_once_with(*args, **kwargs)

    @pytest.mark.parametrize(
        "graph_callable, expected_value",
        ((_GraphCallable(function=type), "type"), (_GraphCallable(function=type, name="test"), "test")),
    )
    def test_name_returns_correct_string(self, graph_callable, expected_value):
        """Ensure _GraphCallable.__str__ returns the correct string"""
        assert graph_callable.name == expected_value

    @pytest.mark.parametrize(
        "invariant1, invariant2, expected_value",
        (
            (_GraphCallable(function=type), _GraphCallable(function=type), True),
            (_GraphCallable(function=type), _GraphCallable(function=help), False),
            (_GraphCallable(function=type, name="type"), _GraphCallable(function=type, name="help"), False),
        ),
    )
    def test_eq(self, invariant1, invariant2, expected_value):
        assert (invariant1 == invariant2) is expected_value
