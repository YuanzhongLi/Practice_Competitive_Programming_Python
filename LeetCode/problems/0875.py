class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ok = max(piles) * len(piles)
        ng = 0
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            tmp = 0
            for p in piles:
                tmp += (p + mid - 1) // mid

            if tmp <= h:
                ok = mid
            else:
                ng = mid

        return ok
