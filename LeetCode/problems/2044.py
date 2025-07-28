# Solution Link: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/solutions/7013644/python-bit-brute-force-solution-with-jap-6pdv/


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        N = len(nums)

        ma = 0
        for num in nums:
            ma |= num

        ans = 0
        for bit in range(1 << N):
            cur = 0
            for i in range(N):
                if ((bit >> i) & 1) == 1:
                    cur |= nums[i]

            if cur == ma:
                ans += 1

        return ans
