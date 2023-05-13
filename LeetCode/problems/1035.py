class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)
        dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, M+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

        return dp[N][M]
