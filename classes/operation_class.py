class operations:
    def __init__(self, *args):
        self.vals = args

    def __repr__(self):
        if len(self.vals) > 1:
            return f"{self.vals[0]} {self.vals[1]} {self.vals[2]}"
        else:
            return f"{self.vals[0]}"

    def __call__(self, G):
        if len(self.vals) > 1:
            if self.vals[1] == "+":
                return G[self.vals[0]] + G[self.vals[2]]
            elif self.vals[1] == "-":
                return G[self.vals[0]] - G[self.vals[2]]
            elif self.vals[1] == "*":
                return G[self.vals[0]] * G[self.vals[2]]
            elif self.vals[1] == "/":
                if G[self.vals[2]] != 0:
                    return G[self.vals[0]] / G[self.vals[2]]
        else:
            return G[self.vals[0]]
