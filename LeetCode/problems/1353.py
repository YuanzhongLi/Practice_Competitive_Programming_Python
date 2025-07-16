# Solution Link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/?envType=daily-question&envId=2025-07-07

from heapq import heappush, heappop


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort()

        heap = []
        ans = 0
        i = 0
        for d in range(1, 100001):
            while i < N:
                event = events[i]
                s, e = event
                if s <= d:
                    heappush(heap, e)
                    i += 1
                else:
                    break

            while len(heap) > 0 and heap[0] < d:
                heappop(heap)

            if len(heap) > 0:
                heappop(heap)
                ans += 1

        return ans
