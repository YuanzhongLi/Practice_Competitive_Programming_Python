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

n = int(input().rstrip())
v_max = 100005
even = [[0, i] for i in range(v_max)]
odd = [[0, i] for i in range(v_max)]
V = list(map(int, input().rstrip().rsplit()))
for i, v in enumerate(V):
  if i&1:
    odd[v][0] += 1
  else:
    even[v][0] += 1

even.sort(reverse=True)
odd.sort(reverse=True)

en = even[0][1]
en_num = even[0][0]
en2 = even[1][1]
en2_num = even[1][0]

on = odd[0][1]
on_num = odd[0][0]
on2 = odd[1][1]
on2_num = odd[1][0]

if en != on or en_num == en2_num or on_num == on2_num:
  print(n-(en_num + on_num))
else:
  print(n-max(en2_num+on_num, en_num+on2_num))
