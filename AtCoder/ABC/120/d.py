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

class Unionfind:
    def __init__(self, N):
        self.N = N
        self.par = [i for i in range(N)] # 節点
        self.rank = [0 for _ in range(N)] # 木の高さ
        self.size = [1 for _ in range(N)] # 節点が属する木の節点数
        self.treeNum = N # 木の数
    def addNode(self, x): # 節点(木)追加
        self.par[x] = x
        self.rank[x] = 0
        self.size[x] = 1
        self.treeNum += 1
    def root(self, x): # 根を探すと同時に経路上にある節点の親が根になるように代入
        if self.par[x] == x:
            return x
        else:
            self.par[x] = Unionfind.root(self, self.par[x])
            return self.par[x]
    def same(self, x, y):
        return Unionfind.root(self, x) == Unionfind.root(self, y)
    def unite(self, x, y):
        x = Unionfind.root(self, x)
        y = Unionfind.root(self, y)
        if x == y:
            return 0
        self.treeNum -= 1
        ret = self.size[x] * self.size[y]
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]            
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return ret

    def group(self):
      ret = []
      fixed = [False for _ in range(self.N)]
      for i in range(self.N):
        if (not fixed[i]):
          tmp = []
          for j in range(i, self.N):
            if Unionfind.same(self, i, j):
              tmp.append(j)
              fixed[j] = True
          ret.append(tmp)

      return ret

N, M = map(int, input().rstrip().rsplit())

bridges = VVI(M,2)
for i in range(M):
  a, b = map(int, input().rstrip().rsplit())
  bridges[i] = a-1, b-1
  
bridges.reverse()

tmp = N * (N-1) // 2

ans = [tmp]

uf = Unionfind(N)
for i in range(M-1):
  a, b = bridges[i]
  cnt = uf.unite(a, b)
  tmp -= cnt
  ans.append(tmp)
  
ans.reverse()

for i in range(M):
  print(ans[i])


