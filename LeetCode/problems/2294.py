# Solution Link: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/solutions/6859524/python-sort-and-greedy-solution-with-jap-vlvz/


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()

        ans = 1
        mi = nums[0]
        for i in range(1, N):
            num = nums[i]
            if num - mi > k:
                ans += 1
                mi = num

        return ans
