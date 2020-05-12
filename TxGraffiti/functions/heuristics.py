def Theo(conjs):
    conjs = list(filter(None, conjs))
    expressions = list(set([c.get_expression() for c in conjs]))
    C = []
    for expression in expressions:
        exp_temp = []
        for c in conjs:
            if c.get_expression() == expression:
                exp_temp.append(c)
        exp_temp.sort(reverse=True, key=lambda x: len(x.hyp_graphs()))
        C.append(exp_temp[0])

    C.sort(reverse=True, key=lambda x: x.touch())
    return C


"""
def Theo(conjs):
    conjs = list(filter(None, conjs))
    conjs = [x for x in conjs if not any(x <= y for y in conjs if x.get_expression() == y.get_expression())]
    conjs.sort(reverse = True, key = lambda x: x.touch())
    return conjs
"""

def Dalmation(conjs):
    conjs = set(conjs)
    return [x for x in conjs 
            if not any(set(x.sharp_graphs()) <= set(y.sharp_graphs()) 
            for y in conjs-{x})]