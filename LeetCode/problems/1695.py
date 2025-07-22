# Solution Link: https://leetcode.com/problems/maximum-erasure-value/description/?envType=daily-question&envId=2025-07-22


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, 0
        s = nums[0]
        se = set([nums[0]])
        ans = s
        while r < N - 1:
            if nums[r + 1] in se:
                se.remove(nums[l])
                s -= nums[l]
                l += 1
            else:
                se.add(nums[r + 1])
                s += nums[r + 1]
                ans = max(s, ans)
                r += 1

        return ans
