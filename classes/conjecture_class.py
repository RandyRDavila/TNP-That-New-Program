
from functions.get_graph_data import get_graph_data


class type_one_conjecture:
    def __init__(self, *args):
        self.statement = args


    def __repr__(self):
        s = f'If {self.statement[0]}, then '
        s += f'{self.statement[1]}'
        s += f' {self.statement[2]}'
        s += f' {self.statement[3]}'
        s += f' {self.statement[4]}'
        s += f' {self.statement[5]}'
        return s


    def __call__(self, G):
        if self.statement[0](G) == True:
            if self.statement[2] == '<=':
                if self.statement[4] == '+':
                    return G[self.statement[1]] <= self.statement[3] + G[self.statement[5]]
                elif self.statement[4] == '-':
                    return G[self.statement[1]] <= self.statement[3] - G[self.statement[5]]
                elif self.statement[4] == '*':
                    return G[self.statement[1]] <= self.statement[3] * G[self.statement[5]]
                else:
                    return G[self.statement[1]] <= self.statement[3] / G[self.statement[5]]
        else:
            return True


    def sharp_check(self, G):
        if self.statement[0](G) == True:
            if self.statement[4] == '+':
                return G[self.statement[1]] == self.statement[3] + G[self.statement[5]]
            elif self.statement[4] == '-':
                return G[self.statement[1]] == self.statement[3] - G[self.statement[5]]
            elif self.statement[4] == '*':
                return G[self.statement[1]] == self.statement[3] * G[self.statement[5]]
            else:
                return G[self.statement[1]] <= self.statement[3] / G[self.statement[5]]
        else:
            return False


    def sharp_graphs(self):
        graphs = get_graph_data()
        return [G for G in graphs 
                if self.statement[0](graphs[G]) == True and self.sharp_check(graphs[G]) == True]


    def scaled_touch_number(self):
        graphs = get_graph_data()
        graphs = [graphs[G] for G in graphs]
        graphs = [G for G in graphs if self.statement[0](G) == True]
        return len(self.sharp_graphs())/len(graphs) + len(graphs)

    
