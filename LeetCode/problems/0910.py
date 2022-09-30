class Solution:
    def smallestRangeII(self, A: List[int], k: int) -> int:
        A.sort()
        ans = A[-1] - A[0]
        for i in range(len(A)-1):
            a = A[i]
            ma = max(a + k, A[-1] - k)
            mi = min(A[0] + k, A[i+1] - k)
            ans = min(ans, abs(ma - mi))

        return ans
