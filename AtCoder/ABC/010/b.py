from sys import stdin
input = stdin.readline
import copy as cp

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
    return self.first < pi.second

def POW(x, n):
  ret = 1
  while n:
    if n&1:
      ret *= x
    x *= x
    n >>= 1
  return ret

ok = [9, 7, 3, 1]

def f(a):
  for i in range(4):
    if a >= ok[i]:
      return a - ok[i]

n = int(input().rstrip())

A = list(map(int, input().rstrip().split()))

ans = 0
for i in range(n):
  ans += f(A[i])

print(ans)
