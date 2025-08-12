# Solution Link: https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/solutions/7071668/python-dp-solution-with-japanese-explana-8ym4/

MOD = 10**9 + 7
toPowerX = [[0] for _ in range(6)]
N = 300
for i in range(1, N + 1):
    ix = i
    for j in range(1, 6):
        if ix <= N:
            toPowerX[j].append(ix)
        ix *= i


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        toPower = toPowerX[x]
        X_LEN = len(toPower)
        MAX = 1
        for i in range(1, n + 1):
            if i > len(toPower) - 1:
                break

            ix = toPower[i]
            if ix > n:
                break

            MAX = i

        # memo[m][i]: mを構成する通り数で、i^xがその内の最大
        # i <= MAXが前提
        # -1は未定
        memo = [[-1 for _ in range(MAX + 1)] for _ in range(n + 1)]

        def dp(m, i):
            if memo[m][i] != -1:
                return memo[m][i]

            ix = toPower[i]
            if ix > m:
                memo[m][i] = 0
                return memo[m][i]
            if ix == m:
                memo[m][i] = 1
                return memo[m][i]

            memo[m][i] = 0
            rest_m = m - ix
            for j in range(1, i):
                memo[m][i] += dp(rest_m, j)

            memo[m][i] %= MOD

            return memo[m][i]

        ans = 0
        for i in range(1, MAX + 1):
            ans += dp(n, i)
            ans %= MOD

        return ans
