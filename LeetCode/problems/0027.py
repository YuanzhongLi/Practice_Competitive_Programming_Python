class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        val_cnt = 0
        for num in nums:
            if num !=  val:
                    nums[idx] = num
                    idx += 1
            else:
                val_cnt += 1

        return len(nums) - val_cnt
