INF = float('inf')
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = minimum coins number to make i
        dp = [INF for _ in range(amount+1)]
        dp[0] = 0
        for c in coins:
            for i in range(c, amount+1):
                dp[i] = min(dp[i], dp[i-c]+1)

        if dp[amount] == INF:
            return -1
        else: return dp[amount]
