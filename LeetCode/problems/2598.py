# Solution Link: https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/solutions/7278684/python-mod-solution-with-japanese-explan-x9w4/


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mod_cnt = [0 for _ in range(value)]

        for num in nums:
            if num < 0:
                num += value * ((abs(num) + value - 1) // value)
            mod_cnt[num % value] += 1

        i = 0
        while True:
            for mod, cnt in enumerate(mod_cnt):
                if cnt == 0:
                    return i * value + mod
                mod_cnt[mod] -= 1
            i += 1
