import grinpy as gp


__all__ = ["calc", "graph_property_check"]


def calc(G, invariant):
    return getattr(gp, invariant)(G)


def graph_property_check(G, property):
    if property == "is_planar":
        return gp.check_planarity(G)[0]
    elif property == "is_regular":
        return gp.min_degree(G) == gp.max_degree(G)
    elif property == "is_cubic":
        return gp.min_degree(G) == 3 and gp.max_degree(G) == 3
    elif property == "is_not_K_n":
        return gp.is_isomorphic(G, gp.complete_graph(gp.number_of_nodes(G))) == False
    elif property == "is_triangle_free":
        return set(gp.triangles(G).values()) == {0}
    else:
        return getattr(gp, property)(G)
    