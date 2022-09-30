from collections import deque
class Solution:
    def pushDominoes(self, D: str) -> str:
        N = len(D)
        A = [0 for _ in range(N)]
        U = [False for _ in range(N)]
        q1 = deque([])
        q2 = deque([])
        for i, d in enumerate(D):
            if d == 'L':
                q1.append(i)
                A[i] = -1
            elif d == 'R':
                q1.append(i)
                A[i] = 1

        while len(q1) > 0:
            while len(q1) > 0:
                i = q1.popleft()
                if U[i]:
                    continue
                U[i] = True
                q2.append(i)

            while len(q2) > 0:
                i = q2.popleft()
                if A[i] == -1 and i > 0 and not U[i-1]: # left
                    A[i-1] -= 1
                    q1.append(i-1)
                elif A[i] == 1 and i < N-1 and not U[i+1]: # right
                    A[i+1] += 1
                    q1.append(i+1)

        ret = ''
        for a in A:
            if a == -1:
                ret += 'L'
            elif a == 1:
                ret += 'R'
            else:
                ret += '.'

        return ret
