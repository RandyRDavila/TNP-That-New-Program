from TxGraffiti.functions.get_graph_data import get_graph_data
from TxGraffiti.functions.get_graph_data import get_hypothesis_data
from TxGraffiti.functions.decorators import timer 


__all__ = ['Theo', 'Dalmation', 'Romy']


def Theo(conjs):
    
    C = []
    conjs = list(filter(None, conjs))
    expressions = set([c.get_expression() for c in conjs])

    for expr in expressions:
        temp_expressions = [c for c in conjs if c.get_expression() == expr]
        temp_expressions.sort(key = lambda c: len(c.hyp_graphs()))
        C.append(temp_expressions[-1])

    C.sort(reverse=True, key=lambda x: x.touch())
    
    return C


@timer
def timed_Theo(conjs):
    return Theo(conjs)


###############################################################################

def Dalmation(conjs, data_set = 'test_data'):

    C = []
    C.append(conjs[0])
    graph_data = get_graph_data(data_set)

    observed_graphs = set(conjs[0].sharp_graphs(graphs = graph_data))

    for i in range(1, len(conjs)):
        current_sharp_graphs = set(conjs[i].sharp_graphs(graphs = graph_data))

        if current_sharp_graphs - observed_graphs != set():
            C.append(conjs[i])
            observed_graphs.union(current_sharp_graphs)

    return C



@timer
def timed_Dalmation(conjs, data_set = 'test_data'):
    return Dalmation(conjs)


################################################################################

def Romy(conjs, data_set = 'test_data'):

    conjs = conjs[:1000]
    C = conjs.copy()
    graph_data = get_graph_data(data_set)

    for i in range(len(conjs)):
        first_sharp_graphs = set(conjs[i].sharp_graphs(graphs = graph_data))
        for j in range(i+1, len(conjs)):
            if set(conjs[j].sharp_graphs(graphs = graph_data)) < first_sharp_graphs and \
                conjs[j] in C:
                C.remove(conjs[j])

    return C


@timer
def timed_Romy(conjs, data_set = 'test_data'):
    return Romy(conjs)