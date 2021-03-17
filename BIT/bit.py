# VERIFICATION: Chokudai SpeedRun 001 J
# URL: https://atcoder.jp/contests/chokudai_S001/submissions/20578231

# 0-indexed
class BIT:
  def __init__(self, nin):
    self.n = nin
    self.data = [0 for _ in range(nin)]

  # sum([0, i])
  def sum(self, i):
    ret = 0
    while i >= 0:
      ret += self.data[i]
      i = (i & (i+1)) - 1
    return ret

  # sum([i, j])
  def sum_between(self, i, j):
    if i > j: return 0
    return self.sum(j) - self.sum(i-1)

  # a[i] += x
  def add(self, i, x):
    while i < self.n:
      self.data[i] += x
      i |= i+1
    return

  # a[0]+...+a[ret] >= x
  def lower_bound(x):
    ret = -1
    k = 1
    while 2*k <= self.n:
      k <<= 1

    while k > 0:
      if ret+k < self.n and self.data[ret+k] < x:
        x -= self.data[ret+k]
        ret += k
      k >>= 1

    return ret+1

N = int(input())
A = map(int, input().rstrip().rsplit())
A = [a-1 for a in A]
bit = BIT(N)
ans = 0
for i in range(N):
  ans += i-bit.sum(A[i])
  bit.add(A[i], 1)

print(ans)
