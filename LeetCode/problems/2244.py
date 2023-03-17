from collections import defaultdict

def f(n):
    if n == 1:
        return -1
    m = n // 3
    q = n % 3
    if q == 0:
        return m
    else:
        return m + 1


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        mp = defaultdict(int)
        for t in tasks:
            mp[t] += 1

        ret = 0
        for v in mp.values():
            c = f(v)
            if c == -1:
                return -1
            ret += c

        return ret
