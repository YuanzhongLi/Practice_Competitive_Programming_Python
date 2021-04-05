# hard
from copy import deepcopy as cp
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        valid = []
        def dfs(A):
            N = len(A)
            if N == n:
                valid.append(cp(A))
                return

            for i in range(n):
                flag = True
                for h, w in A:
                    if N == h or i == w or abs(N-h) == abs(i-w):
                        flag = False
                        break
                if flag:
                    A.append([N, i])
                    dfs(A)
                    A.pop()
        for i in range(n):
            dfs([[0, i]])
        ret = []
        for v in valid:
            tmp = [['.' for _ in range(n)] for _ in range(n)]
            for h, w in v:
                tmp[h][w] = 'Q'
            tmp = [''.join(row) for row in tmp]
            ret.append(tmp)
        return ret
