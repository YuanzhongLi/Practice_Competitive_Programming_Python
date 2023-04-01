class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ok = 0
        ng = len(nums)
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if nums[mid] <= target:
                ok = mid
            else:
                ng = mid

        return ok if nums[ok] == target else -1
