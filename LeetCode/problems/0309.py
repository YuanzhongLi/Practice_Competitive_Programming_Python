# dp[i][j] i th day the max number you can get, j = 0 or 1
# dp[i][0] = dp[i-1][0], dp[i-1][1] + vi
# dp[i][1] = dp[i-1][1], dp[i-2][0] - vi
# dp[N][0] -> ans
INF = float('inf')
class Solution:
    def maxProfit(self, A: List[int]) -> int:
        N = len(A)
        dp = [[-INF, -INF] for _ in range(N+1)]
        dp[0][0] = 0
        dp[0][1] = -INF
        dp[1][0] = 0
        dp[1][1] = -A[0]
        for i in range(2, N+1): # i th day
            dp[i][0] = max(dp[i][0], dp[i-1][0])
            if dp[i-1][1] != -INF:
                dp[i][0] = max(dp[i][0], dp[i-1][1] + A[i-1])

            dp[i][1] = max(dp[i][1], dp[i-1][1])
            if dp[i-2][0] != INF:
                dp[i][1] = max(dp[i][1], dp[i-2][0] - A[i-1])

        return dp[N][0]
