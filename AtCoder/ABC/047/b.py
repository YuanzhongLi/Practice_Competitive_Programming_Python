from sys import stdin
input = stdin.readline
import copy as cp
from collections import deque

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

W, H, N = map(int, input().rstrip().split())

grid = VVI(H, W)
for _ in range(N):
  x, y, a = map(int, input().rstrip().split())
  if a == 1:
    for xx in range(x):
      for yy in range(H):
        grid[yy][xx] = 1
  elif a == 2:
    for xx in range(x, W):
      for yy in range(H):
        grid[yy][xx] = 1
  elif a == 3:
    for xx in range(W):
      for yy in range(y):
        grid[yy][xx] = 1
  elif a == 4:
    for xx in range(W):
      for yy in range(y, H):
        grid[yy][xx] = 1

ans = 0
for xx in range(W):
  for yy in range(H):
    ans += grid[yy][xx]

ans = H*W-ans

print(ans)
