MOD = 1000000000 + 7
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        power2 = [1 for _ in range(N+1)]
        for i in range(1, N+1):
            power2[i] = power2[i-1] * 2 % MOD

        r = N-1
        ans = 0
        for l, num in enumerate(nums):
            while nums[r] + num > target and r >= 0:
                r -= 1

            if r < l:
                break

            ans += power2[r-l]
            ans %= MOD

        return ans
