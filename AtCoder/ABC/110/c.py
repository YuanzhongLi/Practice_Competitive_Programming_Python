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

vs1 = [set([]) for _ in range(26)]
vs2 = [set([]) for _ in range(26)]

strS = input().rstrip()
strT = input().rstrip()

N = len(strS)
S = []
T = []
for i in range(N):
  S.append(strS[i])
  T.append(strT[i])

for i in range(len(S)):
  cs = S[i]
  ct = T[i]
  vs1[ord(ct)-ord('a')].add(ord(cs)-ord('a'))
  vs2[ord(cs)-ord('a')].add(ord(ct)-ord('a'))

ok = True
for i in range(26):
  if len(vs1[i]) > 1 or len(vs2[i]) > 1:
    ok = False
    break

if ok:
  print("Yes")
else:
  print("No")
