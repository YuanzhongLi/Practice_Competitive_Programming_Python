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

towers = [0 for _ in range(999)]
towers[0] = 1

for i in range(1, 999):
  towers[i] = towers[i-1] + (i+1)

a, b = map(int, input().rstrip().split())

ans = -1
for i in range(998):
  if towers[i] - a == towers[i+1] - b:
    ans = towers[i]-a
    if ans >= 0:
      break

print(ans)

