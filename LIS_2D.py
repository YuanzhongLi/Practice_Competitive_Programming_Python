from  bisect import bisect_left
from  functools import cmp_to_key

INF = float('inf')

class E:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, e):
        return self.y < e.y

    def __repr__(self):
        return "{0} {1}".format(self.x, self.y)

INF_E = E(INF, INF)

def LIS(A):
    N = len(A)
    ret = [INF_E for _ in range(N)]
    ret[0] = A[0]
    sz = 1
    for i in range(1, N):
        a = A[i]
        if ret[sz-1] < a: # 広義の場合 <=
            ret[sz] = a
            sz += 1
        else:
            ret[bisect_left(ret, a)] = a # 広義の場合 bisect_right

    return ret[:sz]

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        A = []
        for w, h in envelopes:
            A.append(E(h, w))

        def compare(e1, e2): # 狭義
            if e1.x == e2.x:
                return e2.y - e1.y
            else:
                return e1.x - e2.x

        def compare(e1, e2): # 広義
          if e1.x == e2.x:
            return e1.y - e2.y
          else:
            return e1.x - e2.y


        A.sort(key=cmp_to_key(compare))
        lis = LIS(A)
        return len(lis)
