class Solution:
    def rob(self, A: List[int]) -> int:
        # dp[i] i th house maximum
        # dp[i] = max(dp[i-1], dp[i-2]+ ai)
        N = len(A)
        if N == 1: return A[0]
        dp = [0 for _ in range(N+1)]
        dp[1] = A[0]
        for i in range(2, N+1):
            dp[i] = max(dp[i-1], dp[i-2]+A[i-1])
        return dp[N]
