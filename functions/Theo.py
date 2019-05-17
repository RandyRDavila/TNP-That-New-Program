


def Theo(conjs):
    conjs = list(filter(None, conjs)) 
    expressions = list(set([c.get_expression() for c in conjs]))
    C = []
    for expression in expressions:
        exp_temp = []
        for c in conjs:
            if c.get_expression() == expression:
                exp_temp.append(c)
        exp_temp.sort(reverse = True, key = lambda x: len(x.hyp_graphs()))
        C.append(exp_temp[0])

    C.sort(reverse = True, key = lambda x: x.touch())
    return C