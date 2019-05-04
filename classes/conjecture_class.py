class conjecture:
    def __init__(self, hypothesis, conclusion):
        self.hypothesis = hypothesis
        self.conclusion = conclusion

    def __repr__(self):
        return f"If {self.hypothesis}, then {self.conclusion}"

    def __call__(self, G):
        if self.hypothesis(G) == True:
            return self.conclusion(G)
        else:
            return True
