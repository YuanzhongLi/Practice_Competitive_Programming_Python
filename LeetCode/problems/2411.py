# Solution Link: https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/solutions/7017850/python-bit-solution-with-japanese-explan-2boo/


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N = len(nums)

        most_left = [0 for _ in range(32)]
        ans = [1 for _ in range(N)]
        for i in range(N - 1, -1, -1):
            num = nums[i]
            bit = 0
            while num > 0:
                if (num & 1) == 1:
                    most_left[bit] = i
                num >>= 1
                bit += 1

            ans[i] = max(ans[i], max(most_left) - i + 1)

        return ans
