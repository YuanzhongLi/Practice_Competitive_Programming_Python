class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ret = ((k+1) * k) >> 1
        S = set(nums)
        re = 0
        for num in S:
            if num <= k:
                re += 1
                ret -= num

        num = k+1
        while re > 0:
            if num not in S:
                re -= 1
                ret += num
            num += 1

        return ret
