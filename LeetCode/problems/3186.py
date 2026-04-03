# Solution Link: https://leetcode.com/problems/maximum-total-damage-with-spell-casting/solutions/7265839/python-dp-solution-with-japanese-explana-p53q/


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = defaultdict(int)
        for p in power:
            cnt[p] += 1
        nums = list(cnt.keys())
        nums.sort()
        N = len(nums)

        dp = [0 for _ in range(N)]
        for i in range(N):
            num = nums[i]
            d_num = num * cnt[num]
            dp[i] = d_num
            for j in range(i - 1, max(0, i - 3) - 1, -1):
                num_ = nums[j]
                if num_ + 2 < num:
                    dp[i] = max(dp[i], dp[j] + d_num)
                else:
                    dp[i] = max(dp[i], dp[j])

        return dp[N - 1]
