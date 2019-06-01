import grinpy as gp

from tnp._base_classes import _GraphCallable, _NamespaceIterator


class Property(_GraphCallable):
    pass


class _properties(_NamespaceIterator):
    type = Property

    class namespace:
        is_bipartite = Property(function=gp.is_bipartite)
        is_chordal = Property(function=gp.is_chordal)
        has_bridges = Property(function=gp.has_bridges)
        is_connected = Property(function=gp.is_connected)
        is_distance_regular = Property(function=gp.is_distance_regular)
        is_strongly_regular = Property(function=gp.is_strongly_regular)
        is_eulerian = Property(function=gp.is_eulerian)
        # TODO: Add is_planar property to GrinPy
        is_planar = Property(function=lambda G: gp.check_planarity(G)[0], name="is_planar")
        is_regular = Property(function=gp.is_regular)
        is_cubic = Property(function=gp.is_cubic)
        is_not_K_n = Property(function=lambda G: not gp.is_complete_graph(G), name="is_not_K_n")
        is_triangle_free = Property(function=gp.is_triangle_free)
        is_claw_free = Property(function=gp.is_claw_free)
        is_complete = Property(function=gp.is_complete_graph, name="is_complete")
        # TODO: Add 2-connected


properties = _properties()
