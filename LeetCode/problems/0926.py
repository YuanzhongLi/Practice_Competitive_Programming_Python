class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        left1 = 0
        right0 = 0
        for ch in s:
            if ch == '0':
                right0 += 1

        ret = 1000000
        N = len(s)
        for i in range(N+1):
            if i > 0:
                if s[i-1] == '0':
                    right0 -= 1
                else: # s[i-1] == '1'
                    left1 += 1

            ret = min(ret, left1 + right0)

        return ret
