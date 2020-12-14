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

class EratosthenesSieve:
  def __init__(self, N=1):
    self.f = [0 for _ in range(N+1)]
    self.f[0] = self.f[1] = -1
    self.primes = []
    for i in range(2, N+1):
      if self.f[i]:
        continue
      self.primes.append(i)
      self.f[i] = i
      for j in range(i*i, N+1, i):
        if not self.f[j]:
          self.f[j] = i # jの最小の素因数

  def isPrime(self, x):
    return self.f[x] == x

  # 素因数分解
  def factorList(self, x):
    res = []
    while x != 1:
      res.append(self.f[x])
      x //= self.f[x]
    return res

  # 素因数分解(<素因数, 次数>)
  def factor(self, x):
    fl = self.factorList(x)
    if len(fl) == 0:
      return []

    ret = [Pair(fl[0], 0)]

    for p in fl:
      if ret[len(ret)-1].first == p:
        ret[len(ret)-1].second += 1
      else:
        ret.append(Pair(p, 1))

    return ret

N, M = map(int, input().rstrip().rsplit())

es = EratosthenesSieve(100005)
fl = []
for p in es.primes:
  if M % p == 0:
    ele = [p, 0]
    while M % p == 0:
      M //= p
      ele[1] += 1
    fl.append(ele)

if M != 1:
  fl.append([M, 1])

ans = mint(1)
for ele in fl:
  num = ele[1]
  ans *= modcmb(N-1+num, num)

print(ans)
