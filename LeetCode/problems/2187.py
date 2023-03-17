class Solution:
    def minimumTime(self, time: List[int], total: int) -> int:
        ok = 100000000000000000
        ng = 0
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            tmp = 0
            for t in time:
                tmp += (mid // t)

            if tmp >= total:
                ok = mid
            else:
                ng = mid

        return ok
