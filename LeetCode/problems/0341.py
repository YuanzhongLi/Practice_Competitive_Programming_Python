from collections import deque
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        A = []
        def rec(nestedList):
            for nested_integer in nestedList:
                if nested_integer.isInteger():
                    A.append(nested_integer.getInteger())
                else:
                    rec(nested_integer.getList())
        rec(nestedList)
        self.pos = 0
        self.A = A
        self.N = len(A)

    def next(self) -> int:
        ret = self.A[self.pos]; self.pos+=1
        return ret

    def hasNext(self) -> bool:
         return self.pos < self.N
