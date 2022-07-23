INF = float('inf')
class Solution:
    def minimumDeleteSum(self, S: str, T: str) -> int:
        N = len(S); M = len(T)
        dp = [[INF for _ in range(M+1)] for _ in range(N+1)]
        dp[0][0] = 0
        for i in range(N+1):
            for j in range(M+1):
                if i-1 >= 0 and j-1 >= 0:
                    si = S[i-1]; tj = T[j-1]
                    cost = 0 if si == tj else ord(si) + ord(tj)
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + cost)

                if i-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + ord(S[i-1]))

                if j-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + ord(T[j-1]))

        return dp[N][M]
