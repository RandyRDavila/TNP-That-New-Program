import sys

if sys.version_info[:2] < (3, 4):
    m = "Python 3.6 or later is required for GrinPy (%d.%d detected)."
    raise ImportError(m % sys.version_info[:2])
del sys

import grinpy  # noqa
from grinpy import *  # noqa

import TxGraffiti.functions.make_graph_database  # noqa
from TxGraffiti.functions.make_graph_database import *  # noqa

import TxGraffiti.functions.make_conjectures
from TxGraffiti.functions.make_conjectures import *

import TxGraffiti.functions.make_expressions
from TxGraffiti.functions.make_expressions import *

import TxGraffiti.functions.heuristics 
from TxGraffiti.functions.heuristics import *

import TxGraffiti.functions.make_graph_database
from TxGraffiti.functions.make_graph_database import *

import TxGraffiti.functions.get_graph_data 
from TxGraffiti.functions.get_graph_data import *
