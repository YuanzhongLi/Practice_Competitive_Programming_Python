from copy import deepcopy

INF = 12345678910
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        DP = [triangle[0][0]]
        DP2 = []
        for i in range(1, N):
            DP2 = [INF for _ in range(i+1)]
            DP2[0] = triangle[i][0] + DP[0]
            DP2[i] = triangle[i][i] + DP[i-1]
            print(DP2)
            for j in range(1, i):
                DP2[j] = triangle[i][j] + min(DP[j-1], DP[j])
            DP = deepcopy(DP2)

        return min(DP)
