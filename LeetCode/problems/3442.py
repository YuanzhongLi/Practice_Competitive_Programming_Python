# Solution Link: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/solutions/6827655/python-map-solution-with-japanese-explan-hcaw/


class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = defaultdict(int)
        for ch in s:
            cnt[ch] += 1

        a1, a2 = 1, 10**9
        for val in cnt.values():
            if val % 2 == 0:
                a2 = min(a2, val)
            else:
                a1 = max(a1, val)

        return a1 - a2
