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

S = input().rstrip()
N = len(S)

cnt1 = 0
cnt2 = 0
for i in range(N):
  if ((i & 1) and (S[i] == '0')) or (not(i & 1) and (S[i] == '1')):
    cnt1 += 1

  if ((i & 1) and (S[i] == '1')) or (not(i & 1) and (S[i] == '0')):
    cnt2 += 1


print(min(cnt1, cnt2))



