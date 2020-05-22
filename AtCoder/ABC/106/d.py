from sys import stdin
input = stdin.readline

# map(int, input().rstrip().split())

def VI(N, init=0):
  return [init for _ in range(N)]
def VVI(N, M, init=0):
  return [[init for _ in range(M)] for _ in range(N)]

def VD(N, init=0.0):
  return [init for _ in range(N)]
def VVD(N, M, init=0.0):
  return [[init for _ in range(M)] for _ in range(N)]

N, M, Q = map(int, input().rstrip().split())

table = VVI(N+1, N+1)

for i in range(M):
  L, R = map(int, input().rstrip().split())
  table[L][R] += 1

for i in range(1, N+1):
  for j in range(1, N+1):
    table[i][j] += (table[i][j-1] + table[i-1][j] - table[i-1][j-1])


for i in range(Q):
  p, q = map(int, input().rstrip().split())
  ma = max(p, q)
  mi = min(p, q)
  print(table[ma][ma]-table[ma][mi-1]-table[mi-1][ma]+table[mi-1][mi-1])
