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

H, W = map(int, input().rstrip().rsplit())

grid = []
for i in range(H):
  li = list(map(int, input().rstrip().rsplit()))
  grid.append(li)

ans = []
for i in range(H):
  for j in range(W):
    if j < W-1:
      if grid[i][j]&1:
        grid[i][j] -= 1
        grid[i][j+1] += 1
        ans.append([i, j, i, j+1])
    else:
      if grid[i][j]&1 and i < H-1:
        grid[i][j] -= 1
        grid[i+1][j] += 1
        ans.append([i, j, i+1, j])

print(len(ans))
for li in ans:
  print(' '.join([str(i+1) for i in li]))
