class Solution:
    def maxSatisfaction(self, S: List[int]) -> int:
        S.sort()
        N = len(S)
        tmp = 0
        s = 0
        for i in range(N):
            s += S[i]
            tmp += (i+1) * S[i]

        ans = max(tmp, 0)
        for i in range(1, N):
            tmp -= s
            s -= S[i-1]
            ans = max(ans, tmp)

        return ans
