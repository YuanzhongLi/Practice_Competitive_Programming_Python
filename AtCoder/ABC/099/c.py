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
    return self.first < pi.second

def POW(x, n):
  ret = 1
  while n:
    if n&1:
      ret *= x
    x *= x
    n >>= 1
  return ret

MAX_N = int(1e5+5)

dp = VI(MAX_N, MAX_N)
dp[0] = 0
dp[1] = 1

for i in range(2, MAX_N):
  dp[i] = min(dp[i], dp[i-1]+1)
  for j in range(10):
    six = POW(6, j)
    if six > i:
      break
    else:
      dp[i] = min(dp[i], dp[i-six]+1)

  for j in range(10):
    nine = POW(9, j)
    if nine > i:
      break
    else:
      dp[i] = min(dp[i], dp[i-nine]+1)

N = int(input().rstrip())
print(dp[N])

