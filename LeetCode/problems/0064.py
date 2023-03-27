class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        INF = 1000000000
        H = len(grid)
        W = len(grid[0])
        dp = [[INF for _ in range(W)] for _ in range(H)]
        dp[0][0] = grid[0][0]
        for i in range(H):
            for j in range(W):
                cost = grid[i][j]
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + cost)
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + cost)

        return dp[H-1][W-1]
