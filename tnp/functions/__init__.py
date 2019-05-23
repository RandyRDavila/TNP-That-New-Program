import sys

if sys.version_info[:2] < (3, 4):
    m = "Python 3.4 or later is required for GrinPy (%d.%d detected)."
    raise ImportError(m % sys.version_info[:2])
del sys

import grinpy  # noqa
from grinpy import *  # noqa

import tnp.functions.make_graph_database  # noqa
from tnp.functions.make_graph_database import *  # noqa
