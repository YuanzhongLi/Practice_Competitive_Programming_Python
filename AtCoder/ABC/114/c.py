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

n = int(input().rstrip())

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

ans = 0
def check(b):
  ok3 = False
  ok5 = False
  ok7 = False

  ret = 0
  for i in range(10):
    if b[i] == 1:
      ret += 3*(10**i)
      ok3 = True
    if b[i] == 2:
      ret += 5*(10**i)
      ok5 = True
    if b[i] == 3:
      ret += 7*(10**i)
      ok7 = True

  tmp = ret
  ok = True
  while (tmp):
    rem = tmp % 10
    if rem == 0:
      ok = False
      break
    else:
      tmp //= 10

  return ret, ok3 and ok5 and ok7 and ok

ans = 0
for i in range(1000000):
  bn = baseNumber(4, 10, i)
  X, ok = check(bn)
  if ok and 1 <= X and X <= n:
    ans += 1

print(ans)
