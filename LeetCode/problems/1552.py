class Solution:
    def maxDistance(self, A: List[int], m: int) -> int:
        A.sort()

        def check(l, num):
            pos = A[0]
            idx = 0
            num -= 1
            while num > 0 and idx < len(A):
                if A[idx] >= pos + l:
                    pos = A[idx]
                    num -= 1

                idx += 1

            return num == 0


        ok = 1
        ng = A[-1] - A[0] + 1
        while abs(ok - ng) > 1:
            mid = (ok + ng) >> 1
            if check(mid, m):
                ok = mid
            else:
                ng = mid

        return ok
