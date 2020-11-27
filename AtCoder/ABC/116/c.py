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

def Block(s):
  num = 1
  v1 = []
  v2 = []
  for i in range(len(s)):
    c = s[i]
    if i == 0:
      v1.append(c)
    elif c == s[i-1]:
      num += 1
    else:
      v2.append(num)
      v1.append(c)
      num = 1

    if i == len(s)-1:
      v2.append(num)
  return v1, v2

N = int(input().rstrip())
H = list(map(int, input().rstrip().rsplit()))
ans = 0

while 1:
  cnt = 0
  tmp = VI(N)
  for i in range(N):
    if H[i] > 0:
      tmp[i] = 1
      H[i] -= 1

  b, _ = Block(tmp)

  for i in range(len(b)):
    if b[i]:
      cnt += 1

  ans += cnt
  if cnt == 0:
    break

print(ans)
