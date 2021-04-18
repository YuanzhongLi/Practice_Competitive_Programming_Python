class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        N = len(s)
        prev = s[0]
        cnt = 1
        tot = cost[0]
        ma = cost[0]
        ret = 0
        for i in range(1, N):
            ch = s[i]
            if ch == prev:
                cnt += 1
                tot += cost[i]
                ma = max(ma, cost[i])
            else:
                ret += tot-ma
                prev = ch
                cnt  = 1
                tot = ma = cost[i]
        ret += tot-ma
        return ret
