from heapq import *
from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(list)
        for id, score in items:
            heappush(mp[id], score)
            if len(mp[id]) > 5:
                heappop(mp[id])

        ret = []
        for id, ary in mp.items():
            total = 0
            for score in ary:
                total += score
            ret.append([id, total//5])
        ret.sort()
        return ret
