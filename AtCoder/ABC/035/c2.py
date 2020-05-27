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

class Node:
  def __init__(self, value=0, lazy=0):
    self.value = value
    self.lazy =lazy

class LazySegTree:
  def __init__(self, n_):
    self.n = 1
    while self.n < n_:
      self.n *= 2

    self.e = Node()
    self.dat =  [Node() for _ in range(2*self.n)]

  def eval(self, k, l, r):
    if self.dat[k].lazy != 0:
      self.dat[k].value += self.dat[k].lazy

      if r-l > 1:
        self.dat[2*k+1].lazy += self.dat[k].lazy // 2
        self.dat[2*k+2].lazy += self.dat[k].lazy // 2

      self.dat[k].lazy = 0

  # [l, r)にxを足す
  def add(self, a, b, x, k=0, l=0, r=-1):
    if r < 0:
      r = self.n
    self.eval(k, l, r)
    if b <= l or r <= a:
      return

    if a <= l and r <= b:
      self.dat[k].lazy += (r-l) * x
      self.eval(k, l, r)
    else:
      self.add(a, b, x, 2*k+1, l, (l+r)//2)
      self.add(a, b, x, 2*k+2, (l+r)//2, r)
      self.dat[k].value = self.dat[2*k+1].value + self.dat[2*k+2].value

  def query(self, a, b, k=0, l=0, r=-1):
    if r < 0:
      r = self.n
    if b <= l or r <= a:
      return 0

    self.eval(k, l, r)

    if a <= l and r <= b:
      return self.dat[k].value

    vl = self.query(a, b, 2*k+1, l, (l+r)//2)
    vr = self.query(a, b, 2*k+2, (l+r)//2, r)

    return vl + vr

N, Q = map(int, input().rstrip().split())

lst = LazySegTree(N)
for i in range(Q):
  l, r = map(int, input().rstrip().split())
  l -= 1
  r -= 1
  lst.add(l, r+1, 1)

ans = []
for i in range(N):
  times = lst.query(i, i+1)
  if times % 2 == 0:
    ans.append('0')
  else:
    ans.append('1')

print(''.join(ans))
