class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        ok = 1
        ng = x
        while abs(ok - ng) > 1:
            mid = (ok+ng)//2
            if mid*mid <= x:
                ok = mid
            else:
                ng = mid

        return ok
