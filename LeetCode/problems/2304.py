INF = 1000000007
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[INF for _ in range(n)] for _ in range(m)]
        for col in range(n):
            dp[0][col] = grid[0][col]

        for i in range(m-1):
            for j in range(n):
                num = grid[i][j]
                for k in range(n):
                    dp[i+1][k] = min(dp[i+1][k], dp[i][j] + moveCost[num][k] + grid[i+1][k])

        ret = INF
        for col in range(n):
            ret = min(ret, dp[m-1][col])

        return ret
