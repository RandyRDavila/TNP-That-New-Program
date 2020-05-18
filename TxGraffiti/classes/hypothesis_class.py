class hypothesis:
    """
    A class to represent the hypothesis in a graph theoretic conjecture. 

    ...

    Attributes
    ----------
    *args : list
        A list of strings that name graph theoretic properties.


    Methods
    -------

    """

    def __init__(self, *args):
        self.properties = args

    def __repr__(self):
        s = f"G {self.properties[0]}"
        if len(self.properties) == 1:
            return s
        else:
            for i in range(1, len(self.properties)):
                s += f" and {self.properties[i]}"
        return s

    def __call__(self, G):
        return False not in [G[p] for p in self.properties]

    