from pulp import (
    LpBinary,
    LpMinimize,
    LpProblem,
    LpVariable,
    lpSum,
)

from grinpy import (
    closed_neighborhood,
    is_connected,
    is_dominating_set,
    neighborhood,
    nodes,
    number_of_nodes,
    number_of_nodes_of_degree_k,
    set_neighborhood,
)

import grinpy as gp




def domination_mip(G, show = False):
    prob = LpProblem('Optimal Dominating Set', LpMinimize)

    x_variables = {node: LpVariable('x{}'.format(i+1), 0, 1, LpBinary) 
            for i, node in enumerate(G.nodes())
            }  
    
    S = []
    for key in x_variables:
        S.append(key*x_variables[key])
            
    prob += lpSum([x_variables[n] for n in x_variables])

    x = lambda v, w : int(v in closed_neighborhood(G,w))
    for node in G.nodes():
        prob += lpSum([x(node,n)*x_variables[n]
                        for n in x_variables])>=1
    
    
    
    prob.solve()
    solution_set = {node for node in x_variables if x_variables[node].value() == 1}
    if show == True:
        print(prob)
        print('Solution set:',solution_set)
    
    
    return solution_set


def domination_number(G):
    return len(domination_mip(G))


def total_domination_mip(G, show = False):
    prob = LpProblem('Optimal Total Dominating Set', LpMinimize)

    x_variables = {node: LpVariable('x{}'.format(i+1), 0, 1, LpBinary) 
            for i, node in enumerate(G.nodes())
            }  
    
    S = []
    for key in x_variables:
        S.append(key*x_variables[key])
            
    prob += lpSum([x_variables[n] for n in x_variables])

    x = lambda v, w : int(v in neighborhood(G,w))
    for node in G.nodes():
        prob += lpSum([x(node,n)*x_variables[n]
                        for n in x_variables])>=1
    
    
    
    prob.solve()
    solution_set = {node for node in x_variables if x_variables[node].value() == 1}
    if show == True:
        print(prob)
        print('Solution set:',solution_set)
    
    
    return solution_set


def total_domination_number(G):
    return len(total_domination_mip(G))



def min_independent_dominating_set_ilp(G):
    """Return a smallest independent dominating set in the graph.
    This method solves an integer program to compute a smallest
    independent dominating set. It solves the following integer program:
    minimize
    .. math::
        \\sum_{v \\in V} x_v
    subject to
    ... math::
        x_v + \\sum_{u \\in N(v)} x_u \\geq 1 \\mathrm{ for all } v \\in V
        \\sum_{\\{u, v\\} \\in E} x_u + x_v \\leq 1 \\mathrm{ for all } e \\in E
    where *E* and *V* are the set of edges and nodes of G, and *N(v)* is
    the set of neighbors of the vertex *v*.
    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.
    Returns
    -------
    set
        A set of nodes in a smallest independent dominating set in the
        graph.
    """
    prob = LpProblem('min_total_dominating_set', LpMinimize)
    variables = {
        node: LpVariable('x{}'.format(i+1), 0, 1, LpBinary)
        for i, node in enumerate(G.nodes())
    }

    # Set the domination number objective function
    prob += lpSum(variables)

    # Set constraints for domination
    for node in G.nodes():
        combination = [
            variables[n]
            for n in variables if n in closed_neighborhood(G, node)
        ]
        prob += lpSum(combination) >= 1

    # Set constraints for independence
    for e in G.edges():
        prob += variables[e[0]] + variables[e[1]] <= 1

    prob.solve()
    solution_set = {node for node in variables if variables[node].value() == 1}
    return solution_set


def independent_domination_number(G):
    return len(min_independent_dominating_set_ilp(G))



