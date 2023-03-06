from heapq import heappop, heappush
from functools import cmp_to_key

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ventures = []
        n = len(profits)
        for i in range(n):
            ventures.append([profits[i], capital[i]])

        def comp(a, b):
            if a[1] == b[1]:
                return b[0] - a[0]
            return a[1] - b[1]

        ventures.sort(key=cmp_to_key(comp))
        ventures.reverse()

        heap = []
        while k > 0:
            while len(ventures) > 0 and ventures[-1][1] <= w:
                heappush(heap, -ventures.pop()[0])
            if len(heap) > 0 and k > 0:
                w += -heappop(heap)
                k -= 1
            else:
                break

        return w
