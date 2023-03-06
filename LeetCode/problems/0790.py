MOD = 1000000007

class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[0 for _ in range(5)] for _ in range(n+2)]
        dp[1][0] = 1
        for i in range(2, n+2):
            dp[i][4] = dp[i-2][0]
            dp[i][3] = dp[i-2][0]
            dp[i][2] = dp[i-2][0] + dp[i-1][1]
            dp[i][1] = dp[i-2][0] + dp[i-1][2]
            dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][1] + dp[i][3]
            dp[i][0] %= MOD
            dp[i][1] %= MOD
            dp[i][2] %= MOD
            dp[i][3] %= MOD
            dp[i][4] %= MOD

        return dp[n+1][0]
