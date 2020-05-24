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

MAX_N = 505
MAX_C = 35
D = VVI(MAX_C, MAX_C)
color = VVI(MAX_N, MAX_N)

N, C = map(int, input().rstrip().split())
for i in range(C):
  tmp_list = list(map(int, input().rstrip().split()))
  for j in range(C):
    D[i][j] = tmp_list[j]

for i in range(N):
  tmp_list = list(map(int, input().rstrip().split()))
  for j in range(N):
    color[i][j] = tmp_list[j]
    color[i][j] -= 1

table = VVI(3, MAX_C)

for i in range(N*N):
  x = i % N
  y = i // N
  c = color[y][x]
  for j in range(3):
    if (x+y+2)%3 == j:
      table[j][c] += 1

ans = int(1e9+7)

def dfs(s, diff):
  global ans
  if len(s) >= 3:
    ans = min(ans, diff)
    return

  for c in range(C):
    ddiff = diff
    ss = cp.deepcopy(s)
    if c in s:
      continue

    for i in range(C):
      ddiff += table[len(s)][i] * D[i][c]
    ss.add(c)
    dfs(ss , ddiff)

s = set([])

dfs(s, 0)

print(ans)


