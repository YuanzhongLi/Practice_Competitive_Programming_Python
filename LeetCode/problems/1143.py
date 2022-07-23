class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        N = len(s1); M = len(s2)
        dp = [[0 for _ in range(M+1)]  for _ in range(N+1)]
        for i in range(1, N+1):
            ch1 = s1[i-1]
            for j in range(1, M+1):
                ch2 = s2[j-1]
                dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])
                if ch1 == ch2:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

        return dp[N][M]
