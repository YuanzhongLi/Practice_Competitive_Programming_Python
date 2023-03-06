class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if N < 2:
            return False

        mod_sum = [0 for _ in range(N)]
        for i,num in enumerate(nums):
            mod_sum[i] = nums[i] % k
            if i > 0:
                mod_sum[i] += mod_sum[i-1]
                mod_sum[i] %= k

        s = set([0])
        for i in range(1, N):
            if mod_sum[i] in s:
                return True
            s.add(mod_sum[i-1])

        return False
