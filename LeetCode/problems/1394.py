# Solution Link: https://leetcode.com/problems/find-lucky-integer-in-an-array/description/?envType=daily-question&envId=2025-07-05


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = defaultdict(int)
        for num in arr:
            cnt[num] += 1

        ans = -1
        for key in cnt.keys():
            if key == cnt[key]:
                ans = max(ans, key)

        return ans
