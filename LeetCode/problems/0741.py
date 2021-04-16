INF = float('inf')
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dp = [[-INF for _ in range(N)] for _ in range(N)] # dp[c1][c2]
        dp[0][0] = grid[0][0]
        for t in range(1, 2*N-1):
            dp2 = [[-INF for _ in range(N)] for _ in range(N)]
            for i in range(max(0, t-(N-1)), min(N-1, t)+1):
                for j in range(max(0, t-(N-1)), min(N-1, t)+1):
                    if grid[i][t-i] == -1 or grid[j][t-j] == -1:
                        continue
                    val = grid[i][t-i]
                    if i != j: val += grid[j][t-j]
                    for pi in (i-1, i):
                        for pj in (j-1, j):
                            if pi >= 0 and pj >=0:
                                dp2[i][j] = max(dp2[i][j], dp[pi][pj]+val)
            dp = dp2
        return max(0, dp[N-1][N-1])
