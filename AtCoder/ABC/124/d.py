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

N, K = map(int, input().rstrip().split())
S = input().rstrip()

v1, v2 = Block(S)

zero = []
one = []

if S[0] == '0':
  one.append(0)

for i in range(len(v1)):
  if (v1[i] == '0'):
    zero.append(v2[i])
  else:
    one.append(v2[i])

if S[N-1] == '1':
  zero.append(0)

one.append(0)
zero.append(0)

tmp = 0
for i in range(min(K, len(one)-1)):
  tmp += one[i]
  tmp += zero[i]
  ind = i

ans = tmp
for i in range(len(one)-1):
  ind += 1
  if ind >= len(one):
    break

  ans = max(ans, tmp+one[ind])

  tmp -= (one[i]+zero[i])
  tmp += (one[ind]+zero[ind])

print(ans)





