# Solution Link: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/solutions/7021884/python-enumerate-solution-with-japanese-cdbeu/


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ma = max(nums)
        ans = 1

        cnt = 0
        prev = -1
        for num in nums:
            if num == ma:
                if num == prev:
                    cnt += 1
                else:
                    cnt = 1
            else:
                ans = max(ans, cnt)
                cnt = 0

            prev = num

        ans = max(ans, cnt)

        return ans
