INF = float('inf')
class Solution:
    def jump(self, A: List[int]) -> int:
        N = len(A)
        dp = [INF for _ in range(N)]
        jumps = 0
        cur_end = 0
        far = 0
        for i,a in enumerate(A):
            far = max(far, i+a)
            dp[i] = jumps
            if i == cur_end:
                jumps += 1
                cur_end = far

        return dp[N-1]
