MOD = 1000000007
class Solution:
    def numRollsToTarget(self, n: int, m: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(target + 1):
                for k in range(1, m+1):
                    if j - k >= 0:
                        dp[i][j] += dp[i-1][j - k]
                        dp[i][j] %= MOD
                    else:
                        break

        return dp[n][target]
