class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0 for _ in range(N+1)] for _ in range(N)] # dp[l][r] = max palindrome lengtht of [l, r)
        for i in range(N):
            dp[i][i+1] = 1

        ans = 1
        for length in range(2, N+1):
            for l in range(N - length + 1):
                r = l + length
                dp[l][r] = max(dp[l+1][r], dp[l][r-1])
                if s[l] == s[r-1]:
                    dp[l][r] = max(dp[l][r], dp[l+1][r-1]+2)

                ans = max(ans, dp[l][r])

        return ans
