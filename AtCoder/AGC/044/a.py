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
    return self.first < pi.second

def POW(x, n):
  ret = 1
  while n:
    if n&1:
      ret *= x
    x *= x
    n >>= 1
  return ret

A = 0
B = 0
C = 0
D = 0

mp = OrderedDict({})

def dfs(N):
  global A, B, C, D

  if N in mp:
    return mp[N]

  cost = LINF
  if LINF//D > N:
    cost = D * N

  l = N//2*2
  r = l+2
  if (l//2 < N):
    cost = min(cost, A+(N-l)*D+dfs(l//2))
  if (r//2 < N):
    cost = min(cost, A+(r-N)*D+dfs(r//2))

  l = N//3*3
  r = l+3
  if (l//3 < N):
    cost = min(cost, B+(N-l)*D+dfs(l//3))
  if (r//3 < N):
    cost = min(cost, B+(r-N)*D+dfs(r//3))

  l = N//5*5
  r = l+5
  if (l//5 < N):
    cost = min(cost, C+(N-l)*D+dfs(l//5))
  if (r//5 < N):
    cost = min(cost, C+(r-N)*D+dfs(r//5))

  mp[N] = cost
  return cost


T = int(input().rstrip())

for _ in range(T):
  N, A, B, C, D = map(int, input().rstrip().split())
  mp.clear()
  mp[0] = 0
  mp[1] = D
  ans = dfs(N)
  print(ans)
