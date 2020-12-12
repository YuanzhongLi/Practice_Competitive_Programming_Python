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

N = int(input().rstrip())

data = []

for i in range(N):
  x, y, h = map(int, input().rstrip().rsplit())
  data.append([h, x, y])

data.sort(reverse=True)

def check(cx, cy):
  d = []
  for i in range(N):
    h, x, y = data[i][0], data[i][1], data[i][2]
    d.append([h, abs(x-cx)+abs(y-cy)])

  if d[0][0] == 0:
    H = INF
    for i in range(N):
      H = min(d[i][1])
    if H < 1:
      return INF
    return H
  else:
    H = d[0][0] + d[0][1]
    if H < 1:
      return INF
    ok = True
    for i in range(N):
      if max(H-d[i][1], 0) != d[i][0]:
        ok = False
        break
    if ok:
      return H
    else:
      return INF

find = False
for cx in range(101):
  for cy in range(101):
    ans = check(cx, cy)
    if ans != INF:
      print("{0} {1} {2}".format(cx, cy, ans))
