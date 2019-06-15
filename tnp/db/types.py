import sqlalchemy.types

import tnp.expressions
from tnp.invariants import invariants
from tnp.properties import properties


class ConjectureType(sqlalchemy.types.TypeDecorator):

    impl = sqlalchemy.types.String

    def process_bind_param(self, value, dialect):
        # Convert a tuple containing operator and print string to a
        # comma-separated string of operator name and print string
        _op, _print = value
        return f"{_op.__name__},{_print}"

    def process_result_value(self, value, dialect):
        # Convert a comma-separated string of operator name and print
        # string to a tuple containing operator and print string
        return tuple(value.split(","))

    def copy(self, **kwargs):
        return ConjectureType(self.impl.length)


class Expression(sqlalchemy.types.TypeDecorator):
    impl = sqlalchemy.types.String

    def process_bind_param(self, value, dialect):
        # Convert Expression object to string of simplified expression
        return value.simplified

    def process_result_value(self, value, dialect):
        # Convert string to Expression object
        return tnp.expressions.Expression(value)

    def copy(self, **kwargs):
        return Expression(self.impl.length)


class HypothesesList(sqlalchemy.types.TypeDecorator):
    """Custom SQLAlchemy column type for storing lists of hypotheses."""

    impl = sqlalchemy.types.String

    def process_bind_param(self, value, dialect):
        # Covert list Property objects to comma-separated string of
        # property names
        return ",".join([str(v) for v in value])

    def process_result_value(self, value, dialect):
        # Convert comma-separated string of property names to list of
        # Property objects
        return [properties[v] for v in value.split(",")]

    def copy(self, **kwargs):
        return HypothesesList(self.impl.length)


class Invariant(sqlalchemy.types.TypeDecorator):
    impl = sqlalchemy.types.String

    def process_bind_param(self, value, dialect):
        # Convert Invariant object to string of invariant name
        return value.name

    def process_result_value(self, value, dialect):
        # Convert string of inivariant name to Invariant object
        return invariants[value.name]

    def copy(self, **kwargs):
        return Invariant(self.impl.length)
