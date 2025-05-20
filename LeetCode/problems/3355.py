# Solution Link: https://leetcode.com/problems/zero-array-transformation-i/solutions/6761238/python-imos-solution-with-japanese-explanation/


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        imos = [0 for _ in range(N)]
        for l, r in queries:
            imos[l] -= 1
            if r + 1 <= N - 1:
                imos[r + 1] += 1

        for i in range(1, N):
            imos[i] += imos[i - 1]

        for i, num in enumerate(nums):
            if num + imos[i] > 0:
                return False

        return True
