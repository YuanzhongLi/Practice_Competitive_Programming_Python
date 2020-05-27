class Pair:
  def __init__(self, x=0, y=0):
    self.first = x
    self.second = y

  def __repr__(self):
    return '{0} {1}'.format(self.first, self.second)

  def __lt__(self, pi):
    return self.first < pi.first


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


