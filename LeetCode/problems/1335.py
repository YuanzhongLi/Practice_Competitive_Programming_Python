INF = int(1e18)
class Solution:
    def minDifficulty(self, W: List[int], d: int) -> int:
        N = len(W)
        if N < d:
            return -1

        dp = [[INF for _ in range(N+1)] for _ in range(d+1)]
        for i in range(d+1): dp[i][0] = 0

        for i in range(1, d + 1):
            for j in range(i, N + 1):
                w = 0
                for k in range(j, i - 1, -1):
                    w = max(w, W[k - 1])
                    dp[i][j] = min(dp[i][j], dp[i - 1][k - 1] + w)
        return dp[d][N]
