class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def f(x):
            if x > 0:
                return 1
            elif x == 0:
                return 0
            else:
                return -1
        ans = 1
        for a in nums:
            ans *= f(a)
        return ans
