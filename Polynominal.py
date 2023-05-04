class Polynomial:
    max_degree = 0
    no_zero = False
    def __init__(self, *coefficients):
        odds = {}
        if len(coefficients) != 0:
            copy_odds = {}
            print(type(coefficients[0]))
            j = 0
            if isinstance(coefficients[0], int):
                for i in coefficients:
                    copy_odds[j] = i
                    j += 1
            elif isinstance(coefficients[0], list):
                for i in coefficients[0]:
                    copy_odds[j] = i
                    j += 1
            elif isinstance(coefficients[0], dict):
                for i in coefficients[0]:
                    copy_odds = coefficients[0].copy()
            elif isinstance(coefficients[0], Polynomial):
                copy_odds = coefficients[0].odds
            self.odds = copy_odds.copy()
            print(self.odds)
            self.odds = dict(sorted(self.odds.items()))
            self.__find_zero__()
            self.odds = dict(sorted(self.odds.items()))
            if self.max_degree > 0:
                self.no_zero = True

    def __find_zero__(self):
        for degree, coef in reversed(self.odds.items()):
            if coef == 0:
                self.odds.pop(degree)
            else:
                self.max_degree = degree
                break
        for i in range(self.max_degree):
            if not (i in self.odds.keys()):
                self.odds[i] = 0

    def __repr__(self):
        text = "Polynomial ["
        for i in self.odds:
            text += str(self.odds[i]) + ", "
        return text

    def __str__(self):
        text = ""
        for degree, coef in reversed(self.odds.items()):
            if coef > 0 and degree != self.max_degree:
                text += "+ " + str(coef) + "x^" + str(degree) + " "
            elif coef < 0:
                text += "- " + str(coef) + "x^" + str(degree)
            elif coef > 0 and degree == self.max_degree:
                text += str(coef) + "x^" + str(degree) + " "
        return text

    def __eq__(self, other):
        if isinstance(other,int):
            if self.no_zero == False:
                return self.odds[0] == dother
            else:
                return False
        if len(self.odds) != len(other.odds):
            return False
        else:
            for i in self.odds:
                if self.odds[i] != other.odds[i]:
                    return False
        return True
    def __add__(self, other):
        copy_odds = {}
        if isinstance(other, int):
            copy_odds = self.odds.copy()
            self.copy_odds[0] += other
        else:
            if len(self.odds) < len(other.odds):
                copy_odds = other.odds.copy()
                for i in self.odds:
                    copy_odds[i] += self.odds[i]
                    print(i)
            else:
                copy_odds = self.odds.copy()
                for i in other.odds:
                    copy_odds[i] += other.odds[i]
        return copy_odds
    def __radd__(self, other):
        copy_odds = {}
        if isinstance(other, int):
            copy_odds = self.odds.copy()
            self.copy_odds[0] += other
        else:
            if len(self.odds) < len(other.odds):
                for i in self.odds:
                    copy_odds[i] = (other.odds[i] + self.odds[i])
            else:
                for i in other.odds:
                    copy_odds[i] = other.odds[i] + self.odds[i]
        return copy_odds
    """def __neg__(self):
        copy_odds = {}
        for i in self.odds:
             copy_odds[i] = ~self.odds[i]
        return copy_odds"""

    """def __sub__(self, other):
        copy_odds = {}
        if isinstance(other, int):
            copy_odds = self.odds.copy()
            copy_odds[0]-= other
        else:
            if len(self.odds) > len(other.odds):
                copy_odds = self.odds.copy()
                for i in other.odds:
                    copy_odds[i] -= other.odds[i]
            else:"""




    #def __rsub__(self, other):

    """def __call__(self, x):

    def degree(self):
        return self.max_degree

    def der(self, d=1):

    def __mul__(self, other):

    def __rmul__(self, other):

    def __iter__(self):

    def __next__(self):"""
