import networkx as nx


def graph_property_check(G, property):
	if property == 'is_bipartite':
		return nx.is_bipartite(G)
	elif property == 'is_chordal':
		return nx.is_chordal(G)
	elif property == 'has_bridges':
		return nx.has_bridges(G)
	elif property == 'is_connected':
		return nx.is_connected(G)
	elif property == 'is_distance_regular':
		return nx.is_distance_regular(G)
	elif property == 'is_strongly_regular':
		return nx.is_strongly_regular(G)
	elif property == 'is_eulerian':
		return nx.is_eulerian(G)
	elif property == "is_planar":
		return nx.check_planarity(G)[0]
