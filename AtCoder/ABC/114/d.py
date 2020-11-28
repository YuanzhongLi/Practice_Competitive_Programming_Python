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

N = int(input().rstrip())
si = EratosthenesSieve(N)

mp = {}
for i in range(2, N+1):
  if si.isPrime(i):
    mp[i] = 0

for i in range(2, N+1):
  f = si.factor(i)
  for pi in f:
    mp[pi.first] += pi.second

ans = 0

# 75
for key in mp.keys():
  num = mp[key]
  if num >= 74:
    ans += 1


# 25 * 3
for key in mp.keys():
  num = mp[key]
  for key_ in mp.keys():
    if key_ == key:
      continue
    else:
      num_ = mp[key_]
      if num >= 24 and num_ >= 2:
        ans += 1


# 15 * 5
for key in mp.keys():
  num = mp[key]
  for key_ in mp.keys():
    if key_ == key:
      continue
    else:
      num_ = mp[key_]
      if num >= 14 and num_ >= 4:
        ans += 1

# 5 * 5 * 3
tmp = 0
for key in mp.keys():
  num = mp[key]
  for key_ in mp.keys():
    if key_ == key:
      continue
    else:
      num_ = mp[key_]
      for key__ in mp.keys():
        if key__ == key or key__ == key_:
          continue
        else:
          num__ = mp[key__]
          if num >= 4 and num_ >= 4 and num__ >= 2:
            tmp += 1

ans += tmp//2

print(ans)
