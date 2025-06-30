# Solution Link: https://leetcode.com/problems/longest-harmonious-subsequence/solutions/6900637/python-hashmap-solution-with-japanese-ex-4mou/


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1

        ans = 0
        for key in cnt.keys():
            if (key + 1) in cnt:
                ans = max(ans, cnt[key] + cnt[key + 1])

        return ans
