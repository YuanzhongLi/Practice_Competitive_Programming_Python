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

N = int(input().rstrip())
A = list(map(int, input().rstrip().rsplit()))
B = list(map(int, input().rstrip().rsplit()))

ma_A = [0 for _ in range(N)]
ma_A[0] = A[0]
for i in range(1, N):
  ma_A[i] = max(ma_A[i-1], A[i])

ans = [0 for _ in range(N+1)]
ans[0] = A[0] * B[0]
for i in range(1, N):
  ans[i] = max(max(ans[i-1], ma_A[i-1]*B[i]), A[i] * B[i])

for i in range(N):
  print(ans[i])
