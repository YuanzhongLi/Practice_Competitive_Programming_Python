# easy
# O(N) solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ret = nums[n-1]
        tot = 0
        mi = 0
        for i in range(n-1, -1, -1):
            tot += nums[i]
            ret = max(ret, tot - mi)
            mi = min(mi, tot)
        return ret

# divide and conquer
INF = int(1e18)
class Solution:
    def maxSubArray(self, A: List[int]) -> int:
        def DC(l, r):
            if l >= r:
                return -INF
            half = l + (r-l)//2
            tmp = 0
            ma_left = 0
            for i in range(half-1, l-1, -1):
                tmp += A[i]
                ma_left = max(ma_left, tmp)

            tmp = 0
            ma_right = 0
            for i in range(half+1, r):
                tmp += A[i]
                ma_right = max(ma_right, tmp)

            ret = A[half]+ma_left+ma_right
            ret = max(ret, DC(l, half))
            ret = max(ret, DC(half+1, r))
            return ret

        return DC(0, len(A))
