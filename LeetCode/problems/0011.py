class Solution:
    def maxArea(self, A: List[int]) -> int:
        N = len(A)
        l = 0
        r = N-1
        ret = 0
        while l < r:
            ret = max(ret, min(A[l], A[r])*(r-l))
            if A[l] >= A[r]:
                r -= 1
            else:
                l += 1
        return ret
