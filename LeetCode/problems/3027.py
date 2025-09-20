# Solution Link: https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/solutions/7150226/python-multi-sort-solution-with-japanese-o5vo/

INF = float("inf")


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        N = len(points)
        points.sort(key=lambda point: (-point[1], point[0]))

        ans = 0
        for i in range(N - 1):
            sx, sy = points[i]
            cur_max_x = INF
            for j in range(i + 1, N):
                x, y = points[j]
                if x < sx:
                    continue
                if x < cur_max_x:
                    ans += 1
                    cur_max_x = x

        return ans
