INF = 1 << 30

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)

        l, r = 0, 1
        s = nums[l]
        ans = INF
        while r < N:
            while s < target and r < N:
                s += nums[r]
                r += 1

            while s >= target and l < r:
                ans = min(ans, r - l)
                s -= nums[l]
                l += 1


        return ans if ans != INF else 0
