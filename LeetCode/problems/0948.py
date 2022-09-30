from collections import deque

class Solution:
    def bagOfTokensScore(self, A: List[int], P: int) -> int:
        A.sort()
        q = deque(A)
        ret = 0
        s = 0
        p = P
        while len(q) > 0:
            if p >= q[0]:
                p -= q.popleft()
                s += 1
                ret = max(ret, s)
            else: # p < q[0]
                if s > 0:
                    p += q.pop()
                    s -= 1
                else: # s <= 0
                    break

        return ret
