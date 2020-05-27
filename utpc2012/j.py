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

from heapq import heapify, heappop, heappush, heappushpop

class PriorityQueue:
    def __init__(self, heap):
        '''
        heap ... list
        '''
        self.heap = heap
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)

    def pushpop(self, item):
        return heappushpop(self.heap, item)

    def __call__(self):
        return self.heap

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

class Edge:
  def __init__(self, to, cap, cost, rev):
    self.to = to
    self.cap = cap
    self.cost = cost
    self.rev = rev

class PrimalDual:
  def __init__(self, V):
    self.V = V
    self.G = [[] for _ in range(V)]
    self.potential = VI(V)
    self.min_cost = VI(V)
    self.prevv = VI(V)
    self.preve = VI(V)

  def addEdge(self, ffrom, to, cap, cost):
    self.G[ffrom].append(Edge(to, cap, cost, len(self.G[to])))
    self.G[to].append(Edge(ffrom, 0, -cost, len(self.G[ffrom])-1))

  def minCostFlow(self, s, t, f):
    V = self.V
    ret = 0
    PQ = PriorityQueue([])

    # initialize
    for i in range(V):
      self.potential[i] = 0
      self.preve[i] = -1
      self.prevv[i] = -1

    while f > 0:
      for i in range(V):
        self.min_cost[i] = INF

      PQ.push(Pair(0, s))
      self.min_cost[s] = 0

      while len(PQ) > 0:
        p = PQ.pop()
        if self.min_cost[p.second] < p.first:
          continue
        for i in range(len(self.G[p.second])):
          e = self.G[p.second][i]
          nextCost = self.min_cost[p.second]+e.cost+self.potential[p.second]-self.potential[e.to]
          if (e.cap > 0) and (self.min_cost[e.to] > nextCost):
            self.min_cost[e.to] = nextCost
            self.prevv[e.to] = p.second
            self.preve[e.to] = i
            PQ.push(Pair(self.min_cost[e.to], e.to))

      if self.min_cost[t] == INF:
        return -1

      for v in range(V):
        self.potential[v] += self.min_cost[v]

      add_flow = f

      v = t
      while v != s:
        add_flow = min(add_flow, self.G[self.prevv[v]][self.preve[v]].cap)
        v = self.prevv[v]

      f -= add_flow
      ret += add_flow * self.potential[t]

      v = t
      while v != s:
        e = self.G[self.prevv[v]][self.preve[v]]
        e.cap -= add_flow
        self.G[v][e.rev].cap += add_flow
        v = self.prevv[v]

    return ret

n, m, d = map(int, input().rstrip().split())
src = n+m+d
snk = n+m+d+1
pd = PrimalDual(n+m+d+2)
for key in range(m):
  ls = list(map(int, input().rstrip().split()))
  c = ls[0]
  store = ls[1]-1
  k = ls[2]
  for i in range(3, k+3):
    box = ls[i]-1
    pd.addEdge(n+key, box, 1, c)

  pd.addEdge(n+m+store, n+key, 1, 0)

for store in range(d):
  b = int(input().rstrip())
  pd.addEdge(src, n+m+store, b, 0)

for box in range(n):
  pd.addEdge(box, snk, 1, 0)

ans = pd.minCostFlow(src, snk, n)

print(ans)




