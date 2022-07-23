class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(10000000)
        ok = len(nums) -1
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if nums[mid] >= target:
                ok = mid
            else:
                ng = mid
        return ok
