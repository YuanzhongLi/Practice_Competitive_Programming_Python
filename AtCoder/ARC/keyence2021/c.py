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


MOD = 998244353
class mint:
  def __init__(self, x):
      self.x = x.x if isinstance(x, mint) else x % MOD

  __str__ = lambda self:str(self.x)
  __repr__ = __str__
  __int__ = lambda self: self.x
  __index__ = __int__

  __add__ = lambda self, other: mint(self.x + mint(other).x)
  __sub__ = lambda self, other: mint(self.x - mint(other).x)
  __mul__ = lambda self, other: mint(self.x * mint(other).x)
  __pow__ = lambda self, other: mint(pow(self.x, mint(other).x, MOD))
  __truediv__ = lambda self, other: mint(self.x * pow(mint(other).x, MOD - 2, MOD))
  __floordiv__ = lambda self, other: mint(self.x // mint(other).x)
  __radd__ = lambda self, other: mint(other + self.x)
  __rsub__ = lambda self, other: mint(other - self.x)
  __rpow__ = lambda self, other: mint(pow(other, self.x, MOD))
  __rmul__ = lambda self, other: mint(other * self.x)
  __rtruediv__ = lambda self, other: mint(other * pow(self.x, MOD - 2, MOD))
  __rfloordiv__ = lambda self, other: mint(other // self.x)

  __lt__ = lambda self, other: self.x < mint(other).x
  __gt__ = lambda self, other: self.x > mint(other).x
  __le__ = lambda self, other: self.x <= mint(other).x
  __ge__ = lambda self, other: self.x >= mint(other).x
  __eq__ = lambda self, other: self.x == mint(other).x
  __ne__ = lambda self, other: self.x != mint(other).x

fact = [mint(0) for _ in range(200005)]
fact[0] = mint(1)
for i in range(1, 200005):
  fact[i] = fact[i-1] * mint(i)

def modcmb(n,r):  #nCr = n!/(n-r)!r!
  return fact[n] / fact[r] / fact[n-r]

H, W, K = map(int, input().rstrip().rsplit())
grid = [['' for _ in range(W)] for _ in range(H)]
for i in range(K):
  h,w,c = map(str, input().rstrip().rsplit())
  h = int(h)-1
  w = int(w)-1
  grid[h][w] = c

row_f = [[0 for _ in range(W)] for _ in range(H)]
col_f = [[0 for _ in range(H)] for _ in range(W)]

for i in range(H):
  for j in range(W-2, -1, -1):
    row_f[i][j] = row_f[i][j+1]
    if grid[i][j+1] == '':
      row_f[i][j] += 1

for i in range(W):
  for j in range(H-2, -1, -1):
    col_f[i][j] = col_f[i][j+1]
    if grid[j+1][i] == '':
      col_f[i][j] += 1

mem = [mint(0) for _ in range(max(H, W)+1)]
mem[0] = mint(1)
for i in range(1, len(mem)):
  mem[i] = mem[i-1]
  mem[i] *= mint(3)



dp = [[mint(0) for _ in range(W)] for _ in range(H)]
dp[0][0] = mint(1)
dy = [-1, 0] # u, l
dx = [0, -1]

for x in range(W):
  for y in range(H):
    for i in range(2):
      uy = y + dy[i]
      ux = x + dx[i]
      if 0 <= uy and uy < H and 0 <= ux and ux < W:
        if i == 0: # from up
          if grid[uy][ux] == 'D' or grid[uy][ux] == 'X':
            dp[y][x] += (dp[uy][ux] * mem[row_f[uy][ux]])
          elif grid[uy][ux] == '':
            dp[y][x] += mint(2)*(dp[uy][ux] * mem[row_f[uy][ux]])
        else: # from left
          if grid[uy][ux] == 'R' or grid[uy][ux] == 'X':
            dp[y][x] += (dp[uy][ux] * mem[col_f[ux][uy]])
          elif grid[uy][ux] == '':
            dp[y][x] += mint(2)*(dp[uy][ux] * mem[col_f[ux][uy]])

if grid[H-1][W-1] == '':
  dp[H-1][W-1] *= mint(3)

print(dp[H-1][W-1])
