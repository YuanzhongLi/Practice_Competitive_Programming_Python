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

N, M, X, Y = map(int, input().rstrip().rsplit())
x = list(map(int, input().rstrip().rsplit()))
y = list(map(int, input().rstrip().rsplit()))

x_ma = X
y_mi = Y
for i in range(N):
  x_ma = max(x_ma, x[i])

for i in range(M):
  y_mi = min(y_mi, y[i])

x_ma+=1

if y_mi >= x_ma:
  print("No War")
else:
  print("War")
