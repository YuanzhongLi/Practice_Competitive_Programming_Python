# Solution Link: https://leetcode.com/problems/maximum-difference-between-increasing-elements/solutions/6848290/python-enumerate-solution-by-tada_24-inm2/


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        ans = -1
        mi = nums[0]
        for i in range(1, N):
            ans = max(ans, nums[i] - mi)
            mi = min(mi, nums[i])

        return ans if ans > 0 else -1
