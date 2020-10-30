from sys import stdin
input = stdin.readline
import copy as cp
from collections import deque, OrderedDict

LINF = 1001002003004005006
INF = 10010010010

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

N, A, B, C = map(int, input().rstrip().rsplit())

L = VI(N)
for i in range(N):
  L[i] = int(input().rstrip())

ans = INF
size = POW(4, N)
for i in range(size):
  tmp = i
  ABC = VI(4, 0)
  ABC_cnt = VI(4, 0)
  for j in range(N):
    num = tmp % 4
    ABC[num] += L[j]
    ABC_cnt[num] += 1
    tmp //= 4
  
  ok = True
  for j in range(1, 4):
    if ABC[j] == 0:
      ok = False
      break
  if ok:
    mp = 0
    for j in range(1, 4):
      mp += (ABC_cnt[j]-1)*10
    a = ABC[1]
    b = ABC[2]
    c = ABC[3]
    mp += abs(a-A)+abs(b-B)+abs(c-C)
    ans = min(ans, mp)

print(ans)


