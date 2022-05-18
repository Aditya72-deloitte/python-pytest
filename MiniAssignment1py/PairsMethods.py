from StringMethods import StringClass


class PairsPossible(StringClass):

    def pairs(self):
        result = [(a, b) for idx, a in enumerate(self) for b in self[idx + 1:]]
        print(result)

    def printPairs(self):
        print(self)
