class Solution:
    def shipWithinDays(self, W: List[int], days: int) -> int:
        ok = 500 * len(W)
        ng = 0
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            d = 1
            cap = mid
            flag = True
            for w in W:
                if w > cap:
                    d += 1
                    cap = mid

                if w > cap:
                    flag = False
                    break

                cap -= w

            if flag and d <= days:
                ok = mid
            else:
                ng = mid

        return ok
