from collections import deque
class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        dq = deque([]) # (num, index)
        def update(x, i):
            while dq and x >= dq[-1][0]:
                dq.pop()
            dq.append((x, i))

        N = len(A)
        for i in range(k):
            update(A[i], i)

        ret = [dq[0][0]]
        for i in range(k, N):
            if dq[0][1] <= i-k:
                dq.popleft()
            update(A[i], i)
            ret.append(dq[0][0])

        return ret
