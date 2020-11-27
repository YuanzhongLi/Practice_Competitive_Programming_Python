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

N, X = map(int, input().rstrip().rsplit())

p_mem = VI(51)
t_mem = VI(51)
def init_mem(paty_mem, total_mem):
  paty_mem[0] = 1
  total_mem[0] = 1
  for i in range(1, 51):
    paty_mem[i] = 2*paty_mem[i-1]+1
    total_mem[i] = 2*total_mem[i-1]+3

init_mem(p_mem, t_mem)

ans = 0
level = N
while level >= 0:
  t_num = t_mem[level]
  mid = (t_num+1)//2
  if X == mid:
    ans += 1+p_mem[level-1]
    break
  elif X == 1:
    break
  elif X == t_num:
    ans += p_mem[level]
    break
  elif 1 < X and X < mid:
    if level == 1:
      ans += 1
      break
    X -= 1
  elif mid < X and X < t_num:
    if level == 1:
      ans += 3
      break
    ans += 1 + p_mem[level-1]
    X -= mid

  level -= 1

print(ans)
