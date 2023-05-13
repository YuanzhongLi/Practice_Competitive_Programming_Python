class Solution:
    def mostPoints(self, qs: List[List[int]]) -> int:
        N = len(qs)
        dp = [0 for _ in range(N)]
        dp[N-1] = qs[N-1][0]
        for i in range(N-2, -1, -1):
            q = qs[i]
            p, b = q
            dp[i] = max(dp[i+1], p)
            if i+b+1 < N:
                dp[i] = max(dp[i], dp[i+b+1] + p)

        return dp[0]
