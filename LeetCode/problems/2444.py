def f(nums, mi, ma): # mi <= nums[i] <= ma
    N = len(nums)
    mi_cnt = 0
    ma_cnt = 0
    l = 0
    r = 0
    ret = 0
    if nums[r] == mi:
        mi_cnt += 1
    if nums[r] == ma:
        ma_cnt += 1
    while r < N:
        if mi_cnt > 0 and ma_cnt > 0:
            ret += N - r
            # move l
            if nums[l] == mi:
                mi_cnt -= 1
            if nums[l] == ma:
                ma_cnt -= 1
            l += 1
            # move r
            if l > r:
                r = l
                if r == N:
                    break
                if nums[r] == mi:
                    mi_cnt += 1
                if nums[r] == ma:
                    ma_cnt += 1
        else:
            # move r
            r += 1
            if r == N:
                break
            if nums[r] == mi:
                mi_cnt += 1
            if nums[r] == ma:
                ma_cnt += 1
    return ret

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        tmp = []
        ret = 0
        for num in nums:
            if minK <= num and num <= maxK:
                tmp.append(num)
            else:
                if len(tmp) > 0:
                    ret += f(tmp, minK, maxK)
                    tmp = []

        if len(tmp) > 0:
            ret += f(tmp, minK, maxK)

        return ret
