from sys import stdin
input = stdin.readline
import copy as cp
from collections import deque, OrderedDict

LINF = 1001002003004005006
INF = 1001001001

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

mod = 1000000007
def mint(num):
  return num % mod

# 左づめでの10進数xをdigits桁のN進数vectorにしてを返す
def baseNumber(N, digits, x):
  ret = [0 for _ in range(digits)]
  # 商
  q = x
  cnt = 0
  while q > 0:
    # 余り
    re = q % N
    q //= N
    ret[cnt] = re
    cnt += 1

  return ret

def clac(n1, n2, n3):
  return n3 + n2 * 4 + n1 * 16

N = int(input().rstrip())

dp = VVI(101, 64)

a = 0
c = 1
g = 2
t = 3
agc = 9
acg = 6
gac = 33

def match_out(num):
  if (num == agc or num == acg or num == gac):
    return True
  else:
    return False

for i in range(64):
  if match_out(i):
    dp[3][i] = 0
  else:
    dp[3][i] = 1

for i in range(3, N):
  for j in range(64):
    if match_out(j):
      continue
    vec = baseNumber(4, 3, j)
    # print(vec)
    n1 = vec[2]
    n2 = vec[1]
    n3 = vec[0]
    for n4 in range(4):
      num = clac(n2, n3, n4)
      if (n1 == a and n3 == g and n4 == c) or (n1 == a and n2 == g and n4 == c):
        continue
      if not match_out(num):
        dp[i+1][num] += dp[i][j]
        dp[i+1][num] = mint(dp[i+1][num])

ans = 0
for i in range(64):
  ans += dp[N][i]
  ans = mint(ans)

print(ans)


