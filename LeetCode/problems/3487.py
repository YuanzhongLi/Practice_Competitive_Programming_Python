# Solution Link: https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/solutions/7000857/python-set-solution-with-japanese-explan-ouy6/


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()

        ans = None
        for num in nums:
            if num < 0 or num in s:
                continue

            if ans == None:
                ans = num
            else:
                ans += num

            s.add(num)

        return max(nums) if ans == None else ans
