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

S = input().rstrip()
T = int(input().rstrip())

cnt = 0
x = 0
y = 0
for i in range(len(S)):
  if S[i] == 'L':
    x -= 1
  elif S[i] == 'R':
    x += 1
  elif S[i] == 'U':
    y += 1
  elif S[i] == 'D':
    y -= 1
  else:
    cnt += 1

x = abs(x)
y = abs(y)

ma = x + y + cnt

if (cnt < x):
  x -= cnt
elif (cnt < x+y):
  x = 0
  cnt -= x
  y -= cnt
else:
  cnt -= (x+y)
  x = 0
  y = 0
  x = cnt % 2

mi = x + y

if T == 1:
  print(ma)
else:
  print(mi)



