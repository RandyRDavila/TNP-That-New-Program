from sqlalchemy import Column, Boolean, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

from tnp.invariants import invariants
from tnp.properties import properties


Base = declarative_base()

Graph = type(
    "Graph",
    (Base,),
    {
        "__tablename__": "graphs",
        "id": Column(Integer, primary_key=True),
        "node_link_data": Column(String),
        **{invariant: Column(Numeric) for invariant in invariants.names},
        **{prop: Column(Boolean) for prop in properties.names},
    },
)
