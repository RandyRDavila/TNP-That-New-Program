import sys

if sys.version_info[:2] < (3, 4):
    m = "Python 3.4 or later is required for GrinPy (%d.%d detected)."
    raise ImportError(m % sys.version_info[:2])
del sys

import grinpy
from grinpy import *

import tnp.functions.make_graph_database
from tnp.functions.make_graph_database import *
