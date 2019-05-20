def Theo(conjs):
    conjs = tuple(c for c in conjs if c)
    expressions = set((c.get_expression() for c in conjs))
    theo_conjectures = []
    for expression in expressions:
        conjectures_for_expression = (c for c in conjs if c.get_expression() == expression)
        exp_temp = sorted(conjectures_for_expression, key=lambda x: len(x.hyp_graphs()), reverse=True)
        theo_conjectures.append(exp_temp[0])

    return sorted(theo_conjectures, key=lambda x: x.touch(), reverse=True)
