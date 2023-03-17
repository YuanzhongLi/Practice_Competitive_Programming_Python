from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = defaultdict(int)
        for a in arr:
            mp[a] += 1
        s = set(mp.values())
        return len(s) == len(mp)
