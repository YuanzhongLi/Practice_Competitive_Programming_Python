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

N, T = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

mi = VI(N)
ma = VI(N)

mi[0] = A[0]
ma[N-1] = A[N-1]

for i in range(1, N):
  mi[i] = min(A[i], mi[i-1])

for i in range(N-2, -1, -1):
  ma[i] = max(A[i], ma[i+1])

max_benefit = 0
for i in range(N-1):
  max_benefit = max(max_benefit, ma[i+1]-mi[i])

s = set([])
s.add(A[N-1])
cnt = 0
for i in range(N-2, -1, -1):
  a = A[i]
  if (a+max_benefit) in s:
    cnt += 1
  s.add(a)

print(cnt)
