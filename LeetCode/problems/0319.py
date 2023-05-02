def root(n):
    ok = 1
    ng = n
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if mid * mid <= n:
            ok = mid
        else:
            ng = mid
    return ok

class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0

        return root(n)
