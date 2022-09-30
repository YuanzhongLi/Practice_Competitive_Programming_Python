from collections import deque
class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        N = len(A)
        q = deque([])

        diff = 1000000007
        idx = -1
        for  i, a in enumerate(A):
            d = abs(x - a)
            if d < diff:
                diff = d
                idx = i

        i = idx - 1
        j = idx + 1
        k -= 1
        q.append(A[idx])

        while k > 0:
            if i >= 0 and j < N:
                di = abs(x - A[i])
                dj = abs(x - A[j])
                if di <= dj:
                    q.appendleft(A[i])
                    i -= 1
                else:
                    q.append(A[j])
                    j += 1
            elif i >= 0:
                q.appendleft(A[i])
                i -= 1
            elif j < N:
                q.append(A[j])
                j += 1

            k -= 1
        return list(q)
