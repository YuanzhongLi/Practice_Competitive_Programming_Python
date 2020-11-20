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

N, M = map(int, input().rstrip().rsplit())
A = list(map(int, input().rstrip().rsplit()))
A.sort(reverse=True)
cost = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = VI(N+1, -INF)
dp[0] = 0
for i in range(2, N+1):
  for a in A:
    c = cost[a]
    j = i-c
    if j >= 0:
      new = dp[j]+1
      dp[i] = max(new, dp[i])

tmp = N
ans = []
for i in range(dp[N],0,-1):
  for a in A:
    c = cost[a]
    if tmp-c < 0:
       continue
    if dp[tmp-c] == dp[tmp]-1:
      ans.append(a)
      tmp -= c
      break

print(''.join([str(n) for n in ans]))
