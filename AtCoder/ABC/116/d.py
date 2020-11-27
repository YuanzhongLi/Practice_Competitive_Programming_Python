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

N, K = map(int, input().rstrip().rsplit())
ary = []
for i in range(N):
  t, d = map(int, input().rstrip().rsplit())
  ary.append(Pair(d, t))
ary.sort(reverse=True)

ans = 0
s = set()
ary2 = []
mp = {}
exchange_candidate_sushi = []
for sushi in ary:
  if K > 0:
    t = sushi.second
    d = sushi.first

    if t in s:
      ary2.append(sushi)
    else:
      exchange_candidate_sushi.append(sushi)
      ans += d
      s.add(t)
      mp[t] = 1
      K -= 1
  else:
    break

ans += len(s)**2

ary2.sort(reverse=True)
ary3 = []
for sushi in ary2:
  if K > 0:
    t = sushi.second
    d = sushi.first
    ans += d
    mp[t] += 1
    K -= 1
  else:
    ary3.append(sushi)

ary3.sort(reverse=True)

pq = PriorityQueue([])
for sushi in exchange_candidate_sushi:
  t = sushi.second
  d = sushi.first
  if mp[t] == 1:
    pq.push(sushi)

types = len(s)
for sushi in ary3:
  if len(pq) > 0:
    t = sushi.second
    d = sushi.first

    sushi_ = pq.pop()
    t_ = sushi_.second
    d_ = sushi_.first

    if ans - d_ - types**2 + d + (types-1)**2 > ans:
      ans = ans - d_ - types**2 + d + (types-1)**2
      types -= 1
    else:
      pq.push(sushi)
  else:
    break





print(ans)
