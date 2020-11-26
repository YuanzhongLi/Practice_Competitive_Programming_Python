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

N, M = map(int, input().rstrip().rsplit())

X = list(map(int, input().rstrip().rsplit()))

if N >= M:
  print(0)
else:
  X.sort()
  ans = X[M-1] - X[0]
  diff = []
  for i in range(M-1):
    diff.append(X[i+1]-X[i])

  diff.sort(reverse=True)
  for i in range(N-1):
    ans -= diff[i]

  print(ans)
