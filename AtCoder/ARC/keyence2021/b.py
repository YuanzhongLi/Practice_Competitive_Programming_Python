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


N, K = map(int, input().rstrip().rsplit())
A = list(map(int, input().rstrip().rsplit()))
A.sort()

mem = [0 for _ in range(N)]
for a in A:
  mem[a] += 1

box = [[] for _ in range(K)]

for i in range(N):
  k = 0
  for j in range(mem[i]):
    box[k].append(i)
    k += 1
    if k >= K:
      break

ans = 0
for b in box:
  b.append(INF)
  n = len(b)
  tmp = 0
  for i in range(n):
    if b[i] != i:
      tmp = i
      break
  ans += tmp

print(ans)
