from sys import stdin
input = stdin.readline

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
  def __init__(self, x, y):
    self.first = x
    self.second = y

  def __repr__(self):
    return '{0} {1}'.format(self.first, self.second)

  def __lt__(self, pi):
    return self.first < pi.second

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

si = EratosthenesSieve(51)

def comb(n, r):
  r = min(r, n-r)
  tmp = [0 for _ in range(51)]
  for i in range(n-r+1, n+1):
    f = si.factor(i)
    for pi in f:
      tmp[pi.first] += pi.second

  for i in range(2, r+1):
    f = si.factor(i)
    for pi in f:
      tmp[pi.first] -= pi.second

  ret = 1
  for i in range(51):
    ret *= POW(i, tmp[i])

  return ret

N, A, B = map(int, input().rstrip().split())
V = list(map(int, input().rstrip().split()))
V.sort()
V.reverse()

tot = 0
for i in range(A):
  tot += V[i]

avg = float(tot)/float(A)

l = 0
r = 0
for i in range(N):
  if V[i] == V[A-1]:
    l = i
    break

for i in range(N-1, -1, -1):
  if V[i] == V[A-1]:
    r = i
    break

a_num = r-l+1
aa_num = A-1-l+1

ans = 0
if V[0] == V[A-1]:
  for i in range(A, B+1):
    if i > a_num:
      break
    ans += comb(a_num, i)
else:
  ans += comb(a_num, aa_num)

Decimal(avg)
print(ans)




