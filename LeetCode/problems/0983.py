class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        INF = 1000000000
        dp = [INF for _ in range(366)]
        dp[0] = 0
        D = [False for _ in range(366)]
        for d in days:
            D[d] = True

        for i in range(1, 366):
            if D[i]:
                m_ago = dp[max(i-30, 0)] + costs[2]
                w_ago = dp[max(i-7, 0)] + costs[1]
                d_ago = dp[max(i-1, 0)] + costs[0]
                dp[i] = min(m_ago, w_ago, d_ago)
            else:
                dp[i] = dp[i-1]

        return dp[365]
