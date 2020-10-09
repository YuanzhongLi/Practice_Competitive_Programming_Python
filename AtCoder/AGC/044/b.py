from sys import stdin
input = stdin.readline
import copy as cp
from collections import deque, OrderedDict

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
P = list(map(int, input().rstrip().split()))

grid = VVI(N, N, True)
dist = VVI(N, N)
for i in range(N):
  for j in range(N):
    d = N-1
    d = min(d, i)
    d = min(d, j)
    d = min(d, N-1-i)
    d = min(d, N-1-j)
    dist[i][j] = d

dx = [0, 1, 0, -1] # u, r, d, l
dy = [-1, 0, 1, 0] # u, r, d, l

ans = 0
for p in P:
  p -= 1
  x = p % N
  y = p // N
  ans += dist[y][x]
  grid[y][x] = False
  q = deque([])
  q.append(p)
  while len(q) > 0:
    v = q.popleft()
    vx = v % N
    vy = v // N
    vp = grid[vy][vx]
    for i in range(4):
      ux = vx + dx[i]
      uy = vy + dy[i]
      if 0 <= ux and ux < N and 0 <= uy and uy < N:
        u = uy*N+ux
        nxtd = dist[vy][vx]
        if vp:
          nxtd+=1
        if dist[uy][ux] > nxtd:
          dist[uy][ux] = nxtd
          q.append(u)

print(ans)



