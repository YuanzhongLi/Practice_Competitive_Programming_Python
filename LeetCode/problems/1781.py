INF = 1000000007
def beauty(A):
    mi = INF
    ma = -INF
    non_zero = 0
    for a in A:
        if a != 0:
            non_zero += 1
            mi = min(mi, a)
            ma = max(ma, a)

    if non_zero >= 2:
        return ma - mi
    return 0

class Solution:
    def beautySum(self, s: str) -> int:
        N = len(s)
        mem = [[0 for _ in range(26)] for _ in range(N+1)]
        ord_a = ord('a')
        for i in range(1, N+1):
            ch = s[i-1]
            chi = ord(ch) - ord_a
            mem[i][chi] += 1
            for j in range(26):
                mem[i][j] += mem[i-1][j]

        ans = 0
        tmp = [0 for _ in range(26)]
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                for k in range(26):
                    tmp[k] = mem[j][k] - mem[i-1][k]
                ans += beauty(tmp)

        return ans
