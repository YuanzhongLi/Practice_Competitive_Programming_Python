# Solution Link: https://leetcode.com/problems/find-the-original-typed-string-ii/solutions/6909336/python-dp-and-range-sum-solution-with-ja-tks7/

MOD = 10**9 + 7


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        N = len(word)
        sections = []

        prev_ch = word[0]
        cnt = 1
        for i in range(1, N):
            ch = word[i]
            if ch == prev_ch:
                cnt += 1
            else:
                k -= 1
                if cnt > 1:
                    sections.append(cnt - 1)
                prev_ch = ch
                cnt = 1
        k -= 1
        if cnt > 1:
            sections.append(cnt - 1)

        total = 1
        for x in sections:
            total *= x + 1
            total %= MOD

        if k <= 0:
            return total

        k -= 1

        def getRangeSum(range_sum_dp, i, j):
            if i == 0:
                return range_sum_dp[j]
            return range_sum_dp[j] - range_sum_dp[i - 1]

        dp = [0 for _ in range(k + 1)]
        dp[0] = 1
        for x in sections:
            range_sum_dp = [0 for _ in range(k + 1)]
            range_sum_dp[0] = dp[0]
            for i in range(1, k + 1):
                range_sum_dp[i] = range_sum_dp[i - 1] + dp[i]

            new_dp = [0 for _ in range(k + 1)]
            for i in range(k + 1):
                new_dp[i] = getRangeSum(range_sum_dp, max(0, i - x), i)
            dp = new_dp

        sum_under_k = sum(dp) % MOD
        ans = (total + MOD - sum_under_k) % MOD

        return ans
