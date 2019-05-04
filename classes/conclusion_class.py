from classes.graph_calculator import calc
from fractions import Fraction


class conclusion:
    def __init__(self, target, invariant, inequality, ratio, const):
        self.target = target
        self.invariant = invariant
        self.inequality = inequality
        self.ratio = Fraction(ratio)
        self.const = const

    def __repr__(self):
        if self.const == Fraction(0, 1):
            return f"{self.target} {self.inequality} {self.ratio}*{self.invariant}"
        elif self.ratio == Fraction(1, 1):
            return f"{self.target} {self.inequality} {self.invariant} + {self.const}"
        else:
            return f"{self.target} {self.inequality} {self.ratio}*{self.invariant} + {self.const}"

    def __call__(self, G):
        if self.inequality == "<=":
            return G[self.target] <= (self.ratio * G[self.invariant] + self.const)
        elif self.inequality == ">=":
            return G[self.target] >= self.ratio * G[self.invariant] + self.const
        elif self.inequality == "=":
            return G[self.target] == self.ratio * G[self.invariant] + self.const

    def check_sharp(self, G):
        return G[self.target] == (self.ratio * G[self.invariant] + self.const)
