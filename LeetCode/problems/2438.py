# Solution Link: https://leetcode.com/problems/range-product-queries-of-powers/solutions/7066232/python-range-sum-solution-with-japanese-explanation/

MOD = 10**9 + 7

# 1 + 2 + ... + 32
MAX = (32 + 1) * 32 // 2
MOD_POWER2 = [0 for _ in range(MAX)]
MOD_POWER2[0] = 1
cur = 1
for i in range(1, MAX):
    cur <<= 1
    cur %= MOD
    MOD_POWER2[i] = cur


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        i = 0
        cnt = 0
        while n > 0:
            if (n & 1) == 1:
                powers.append(cnt)

            cnt += 1
            n >>= 1

        N = len(powers)
        s_powers = [0 for _ in range(N)]
        s_powers[0] = powers[0]
        for i in range(1, N):
            s_powers[i] = s_powers[i - 1] + powers[i]

        def range_sum(l, r):
            if l == 0:
                return s_powers[r]

            return s_powers[r] - s_powers[l - 1]

        ans = []
        for l, r in queries:
            ans.append(MOD_POWER2[range_sum(l, r)])

        return ans
