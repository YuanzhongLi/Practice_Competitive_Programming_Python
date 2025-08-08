# Solution Link: https://leetcode.com/problems/soup-servings/solutions/7056287/python-dp-solution-with-japanese-explana-clb0/


class Solution:
    def soupServings(self, n: int) -> float:
        m = (n + 24) // 25
        memo = defaultdict(dict)

        # i: Aの残り, j: Bの残り
        # dp[i][j]: Aが残りiでBが残りjで条件を達成する確率
        def dp(i, j):
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1.0
            if j <= 0:
                return 0.0

            if i in memo and j in memo[i]:
                return memo[i][j]

            memo[i][j] = (
                dp(i - 4, j) + dp(i - 3, j - 1) + dp(i - 2, j - 2) + dp(i - 1, j - 3)
            ) / 4.0

            return memo[i][j]

        for k in range(1, m + 1):
            if dp(k, k) > 1 - 1e-5:
                return 1.0

        return dp(m, m)
