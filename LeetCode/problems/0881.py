from heapq import heapify, heappush, heappop

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        people.sort()
        people.reverse()
        hq = []
        ans = 0
        for p in people:
            if p == limit:
                ans += 1
                continue

            if len(hq) > 0:
                top = -heappop(hq)
                if top >= p:
                    ans += 1
                else:
                    heappush(hq, -top)
                    heappush(hq, -(limit - p))
            else:
                heappush(hq, -(limit - p))

        ans += len(hq)
        return ans
