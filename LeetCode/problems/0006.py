# NlogN solution
class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1: return s
        ret = []
        r = c = 0
        state = 0
        for ch in s:
            if state == 0:
                ret.append((r, c, ch))
                r += 1
                if r == n:
                    r -= 2
                    c += 1
                    state = 1
            else:
                ret.append((r, c, ch))
                r -= 1
                if r == -1:
                    r = 1
                    state = 0
                else:
                    c += 1

        ret.sort()
        ret = ''.join([ch for _, _, ch in ret])
        return ret
