# Solution Link: https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/solutions/6936972/python-range-sum-solution-with-japanese-rgdi7/


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        N = len(startTime)

        spaces = []

        prev_e = 0
        for i in range(N):
            s, e = startTime[i], endTime[i]
            spaces.append(s - prev_e)
            prev_e = e
        spaces.append(eventTime - prev_e)

        ans = 0
        for i in range(k + 1):
            ans += spaces[i]

        cur = ans
        for i in range(k + 1, N + 1):
            cur += spaces[i] - spaces[i - k - 1]
            ans = max(ans, cur)

        return ans
