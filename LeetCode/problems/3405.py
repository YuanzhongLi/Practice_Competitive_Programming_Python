# Solution Link: https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/solutions/6852186/python-math-solution-with-japanese-expla-cxno/

MOD = 10**9 + 7
MAX = 100005


class mint:
    def __init__(self, x):
        self.x = x.x if isinstance(x, mint) else x % MOD

    __str__ = lambda self: str(self.x)
    __repr__ = __str__
    __int__ = lambda self: self.x
    __index__ = __int__

    __add__ = lambda self, other: mint(self.x + mint(other).x)
    __sub__ = lambda self, other: mint(self.x - mint(other).x)
    __mul__ = lambda self, other: mint(self.x * mint(other).x)
    __pow__ = lambda self, other: mint(pow(self.x, mint(other).x, MOD))
    __truediv__ = lambda self, other: mint(self.x * pow(mint(other).x, MOD - 2, MOD))
    __floordiv__ = lambda self, other: mint(self.x // mint(other).x)
    __radd__ = lambda self, other: mint(other + self.x)
    __rsub__ = lambda self, other: mint(other - self.x)
    __rpow__ = lambda self, other: mint(pow(other, self.x, MOD))
    __rmul__ = lambda self, other: mint(other * self.x)
    __rtruediv__ = lambda self, other: mint(other * pow(self.x, MOD - 2, MOD))
    __rfloordiv__ = lambda self, other: mint(other // self.x)

    __lt__ = lambda self, other: self.x < mint(other).x
    __gt__ = lambda self, other: self.x > mint(other).x
    __le__ = lambda self, other: self.x <= mint(other).x
    __ge__ = lambda self, other: self.x >= mint(other).x
    __eq__ = lambda self, other: self.x == mint(other).x
    __ne__ = lambda self, other: self.x != mint(other).x


fact = [mint(0) for _ in range(MAX)]
fact[0] = mint(1)
for i in range(1, MAX):
    fact[i] = fact[i - 1] * mint(i)


def modcmb(n, r):  # nCr = n!/(n-r)!r!
    return fact[n] / fact[r] / fact[n - r]


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        ans = modcmb(n - 1, k) * mint(m) * (mint(m - 1) ** (n - k - 1))
        return ans.x
