class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sn = len(s); tn = len(t)
        dp = [[0 for _ in range(tn+1)] for _ in range(sn+1)]
        for i in range(sn+1):
            dp[i][0] = 1
        for i in range(1,sn+1):
            for j in range(1, tn+1):
                dp[i][j] += dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]

        return dp[sn][tn]
