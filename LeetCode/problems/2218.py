class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        N = len(piles)
        dp = [[0 for _ in range(k+1)] for _ in range(N + 1)]
        for i in range(1, N+1):
            for coins in range(k+1):
                cur_sum = 0
                for cur_coins in range(min(len(piles[i-1]), coins) + 1):
                    if cur_coins > 0:
                        cur_sum += piles[i-1][cur_coins - 1]
                    dp[i][coins] = max(dp[i][coins], dp[i-1][coins - cur_coins] + cur_sum)

        return dp[N][k]
