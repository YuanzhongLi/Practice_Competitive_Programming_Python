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

from math import gcd

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

gcd_l = VI(N)
gcd_r = VI(N)

for i in range(N):
  i_ = N-1-i
  if i == 0:
    gcd_l[i] = A[i]
    gcd_r[i_] = A[i_]
  else:
    gcd_l[i] = gcd(A[i], gcd_l[i-1])
    gcd_r[i_] = gcd(A[i_], gcd_r[i_+1])

ans = 1

for i in range(N):
  if i == 0:
    ans = max(ans, gcd_r[i+1])
  elif i == N-1:
    ans = max(ans, gcd_l[i-1])
  else:
    ans = max(ans, gcd(gcd_l[i-1], gcd_r[i+1]))

print(ans)

