from sys import stdin
input = stdin.readline
import copy as cp
from collections import deque, OrderedDict

INF = 1001002003004005006

def VI(N, init=0):
  return [init for _ in range(N)]
def VVI(N, M, init=0):
  return [[init for _ in range(M)] for _ in range(N)]

def VD(N, init=0.0):
  return [init for _ in range(N)]
def VVD(N, M, init=0.0):
  return [[init for _ in range(M)] for _ in range(N)]

def Decimal(x):
  print("{0:.10f}".format(x))

class Pair:
  def __init__(self, x=0, y=0):
    self.first = x
    self.second = y

  def __repr__(self):
    return '{0} {1}'.format(self.first, self.second)

  def __lt__(self, pi):
    return self.first < pi.first

def POW(x, n):
  ret = 1
  while n:
    if n&1:
      ret *= x
    x *= x
    n >>= 1
  return ret

MOD = 10**9 + 7
class mint:
  def __init__(self, x):
      self.x = x.x if isinstance(x, mint) else x % MOD

  __str__ = lambda self:str(self.x)
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

fact = [mint(0) for _ in range(200005)]
fact[0] = mint(1)
for i in range(1, 200005):
  fact[i] = fact[i-1] * mint(i)

def modcmb(n,r):  #nCr = n!/(n-r)!r!
  return fact[n] / fact[r] / fact[n-r]

H, W, A, B = map(int, input().rstrip().rsplit())

ans = mint(0)
for i in range(1, W-B+1):
  ans += (modcmb(H-A-1 + B+i-1, B+i-1) * modcmb(A-1 + W-(B+i), W-(B+i)))

print(ans)
