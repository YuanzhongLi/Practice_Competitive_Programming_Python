from heapq import *
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)//2
        hq = []
        ret = 0
        for a, b in costs:
            ret += a
            heappush(hq, b-a)

        for _ in range(N):
            ret += heappop(hq)

        return ret
