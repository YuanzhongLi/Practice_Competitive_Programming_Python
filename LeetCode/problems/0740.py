# 2, 2, 3, 3, 3, 4, 4...
# 2: 3, 3: 3, 4: 2, 5: 3, 6: 4, …
# dp[i] the max point you can get i = num
MAX = 10005
class Solution:
    def deleteAndEarn(self, A: List[int]) -> int:
        counter = [0 for _ in range(MAX)]
        for a in A:
            counter[a] += 1

        dp = [0 for _ in range(MAX)]
        dp[1] = counter[1]
        for i in range(1, MAX):
            dp[i] = max(dp[i], dp[i-1])
            if i >= 2:
                dp[i] = max(dp[i], dp[i-2]+ i * counter[i])

        return dp[MAX-1]
