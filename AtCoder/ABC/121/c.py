from sys import stdin
input = stdin.readline
import copy as cp
from collections import deque, OrderedDict
from functools import cmp_to_key

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

N, M = map(int, input().rstrip().split())
AB = VVI(N, 2)

for i in range(N):
  a, b = map(int, input().rstrip().split())
  AB[i][0] = a
  AB[i][1] = b

def cmp(a, b):
  if a[0] == b[0]:
    return 0
  elif a[0] < b[0]:
    return -1
  else:
    return 1

AB.sort(key=cmp_to_key(cmp))

ans = 0

for i in range(N):
  while M > 0 and AB[i][1] > 0:
    ans += AB[i][0]
    M -= 1
    AB[i][1] -= 1

print(ans)




