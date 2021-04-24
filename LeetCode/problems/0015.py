INF = float('inf')
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        if N <= 2:
            return []

        ans = []
        prev_a = -INF
        for i in range(N):
            a = nums[i]
            if a > 0:
                break
            if i == 0 or prev_a != a:
                l, r = i+1, N-1
                while l < r:
                    s = a + nums[l] + nums[r]
                    if s < 0:
                        l += 1
                    elif s > 0:
                        r -= 1
                    else:
                        ans.append([a, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
            prev_a = a

        return ans
