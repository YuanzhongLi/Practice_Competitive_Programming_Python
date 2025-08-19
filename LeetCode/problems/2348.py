# Solution Link: https://leetcode.com/problems/number-of-zero-filled-subarrays/solutions/7097165/python-math-solution-with-japanese-expal-ar5x/


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # 1 + 2 + ... + xを返す
        def func(x):
            return x * (x + 1) // 2

        ans = 0
        prev_is_0 = False
        cnt0 = 0
        for num in nums:
            if num == 0:
                if prev_is_0:
                    cnt0 += 1
                else:
                    cnt0 = 1
                    prev_is_0 = True
            else:
                if prev_is_0:
                    ans += func(cnt0)
                    cnt0 = 0
                    prev_is_0 = False

        ans += func(cnt0)

        return ans
