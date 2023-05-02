from heapq import heappush, heappop, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        N = len(stones)
        for i in range(N):
            stones[i] = -stones[i]

        heapify(stones)
        while len(stones) >= 2:
            stone1 = -heappop(stones)
            stone2 = -heappop(stones)
            if stone1 > stone2:
                heappush(stones, -(stone1-stone2))

        if stones:
            return -stones[0]

        return 0
