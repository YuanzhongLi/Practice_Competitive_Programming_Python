INF = 1000000007
class Solution:
    def maxProfit(self, k: int, P: List[int]) -> int:
        N = len(P)
        dp = [[[0, -INF] for _ in range(k+1)] for _ in range(N+1)]

        ans = 0
        for n in range(1, N+1):
            for l in range(k+1):
                if l > 0:
                    dp[n][l][0] = max(dp[n-1][l][0], dp[n-1][l-1][1] + P[n-1])
                ans = max(ans, dp[n][l][0])
                dp[n][l][1] = max(dp[n-1][l][1], dp[n-1][l][0] - P[n-1])

        return ans
