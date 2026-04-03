# Solution Link: https://leetcode.com/problems/triangle/solutions/7221511/python-in-place-dp-solution-with-japanes-ifp0/


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        if N == 1:
            return triangle[0][0]

        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]

        for i in range(2, N):
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][i] += triangle[i - 1][i - 1]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])

        return min(triangle[N - 1])
