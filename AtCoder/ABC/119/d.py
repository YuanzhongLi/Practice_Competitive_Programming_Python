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

A, B, Q = map(int, input().rstrip().split())

S = VI(A+2)
S[0] = -INF
S[len(S)-1] = INF

T = VI(B+2)
T[0] = -INF
T[len(T)-1] = INF

for i in range(1, len(S)-1):
  S[i] = int(input().rstrip())
  
  
for i in range(1, len(T)-1):
  T[i] = int(input().rstrip())
  
def bs_S(x):
  ok, ng = len(S)-1, -1
  while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if S[mid] >= x:
      ok = mid
    else:
      ng = mid
  return ok
  
def bs_T(x):
  ok, ng = len(T)-1, -1
  while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if T[mid] >= x:
      ok = mid
    else:
      ng = mid
  return ok
    
  
for i in range(Q):
  x = int(input().rstrip())
  sri = bs_S(x)
  sli = sri-1
  tri = bs_T(x)
  tli = tri-1
  
  sr = S[sri]
  sl = S[sli]
  tr = T[tri]
  tl = T[tli]
  
  ans = INF
  ans = min(ans, max(sr, tr) - x)
  ans = min(ans, x-min(sl, tl))
  ans = min(ans, sr-x + sr-tl)
  ans = min(ans, tr-x + tr-sl)
  ans = min(ans, x-sl + tr-sl)
  ans = min(ans, x-tl + sr-tl)
  
  print(ans)
  
  
