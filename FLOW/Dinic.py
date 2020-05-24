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
    return self.first < pi.second

def POW(x, n):
  ret = 1
  while n:
    if n&1:
      ret *= x
    x *= x
    n >>= 1
  return ret

# VERIFICATION: ABC 10_D
# URL: https://atcoder.jp/contests/abc010/submissions/13576437

class Edge:
  def __init__(self, to:int=0, cap=0, rev:int=0):
    self.to = to
    self.cap = cap
    self.rev = rev

class Dinic:
  def __init__(self, V:int, INF=int(1e9+7)):
    self.INF = INF
    self.V = V
    self.G = [[] for _ in range(V)]
    self.level = [0 for _ in range(V)]
    self.used = [False for _ in range(V)]

  def addEdge(self, ffrom:int, to:int, cap):
    self.G[ffrom].append(Edge(to, cap, len(self.G[to])))
    self.G[to].append(Edge(ffrom, 0, len(self.G[ffrom])-1))

  def bfs(self, s:int):
    for i in range(self.V):
      self.level[i] = -1
      q = deque([])
      self.level[s] = 0
      q.append(s)
      while len(q) > 0:
        v = q.popleft()
        for e in self.G[v]:
          if e.cap > 0 and self.level[e.to] < 0:
            self.level[e.to] = self.level[v]+1
            q.append(e.to)

  def dfs(self, v:int, t:int, f):
    if v == t:
      return f

    self.used[v] = True
    for i in range(len(self.G[v])):
      e = self.G[v][i]
      if e.cap > 0 and self.level[v] < self.level[e.to] and (not self.used[e.to]):
        d = self.dfs(e.to, t, min(f, e.cap))
        if d > 0:
          e.cap -= d
          self.G[e.to][e.rev].cap += d
          return d

    return 0

  def max_flow(self, s:int, t:int):
    ret = 0
    f = 0

    self.bfs(s)
    while self.level[t] >= 0:
      for i in range(self.V):
        self.used[i] = False

      f = self.dfs(s, t, self.INF)
      while f > 0:
        ret += f
        f = self.dfs(s, t, self.INF)

      self.bfs(s)

    return ret


