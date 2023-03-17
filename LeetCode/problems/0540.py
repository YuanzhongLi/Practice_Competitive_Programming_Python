class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def dfs(l, r):
            if r - l == 1:
                return nums[l]
            if (r - l) % 2 == 0:
                return -1

            mid = (r+l)//2

            if nums[mid-1] == nums[mid]:
                return max(dfs(l, mid+1), dfs(mid+1, r))
            else: # nums[mid] == nums[mid+1]
                return max(dfs(l, mid), dfs(mid, r))

        return dfs(0, len(nums))
