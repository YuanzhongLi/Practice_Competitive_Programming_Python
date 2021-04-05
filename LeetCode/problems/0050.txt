class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        ret = 1.0
        if n >= 0: # x^2, x^4, x^8, ...
            while n > 0:
                if (n&1) == 1:
                    ret *= x
                x *= x
                n >>= 1
            return ret
        else: # x^-2, x^-4, ...
            x = 1.0/x
            n = abs(n)
            while n > 0:
                if (n&1) == 1:
                    ret *= x
                x *= x
                n >>= 1
            return ret
