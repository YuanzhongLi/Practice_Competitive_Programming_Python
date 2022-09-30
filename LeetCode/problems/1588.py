class Solution:
    def sumOddLengthSubarrays(self, A: List[int]) -> int:
        N = len(A)
        if N == 1 or N == 2:
            return sum(A)

        dp = [0 for _ in range(N)]
        dp[0] = A[0]
        dp[1] = A[1]
        ans = A[0] + A[1]
        for i in range(2, N):
            dp[i] = dp[i-2]
            dp[i] += (i // 2) * (A[i] + A[i-1]) + A[i]
            ans += dp[i]

        return ans
