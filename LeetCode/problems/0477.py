class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            o = 0
            z = 0
            for n in nums:
                if ((n>>i)&1) == 0:
                    o += 1
                else:
                    z += 1
            ans += o*z

        return ans
